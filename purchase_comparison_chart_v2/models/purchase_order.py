from odoo import models, fields,api,_
from urllib.parse import urljoin
from odoo.addons.website.models.website import slugify
from odoo.exceptions import UserError
import xlwt
import base64
from datetime import datetime

from werkzeug.urls import url_encode
import werkzeug

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'   

    @api.depends('order_line.invoice_lines.invoice_id','invoice_ids')
    def _compute_invoice(self):
            #self.invoice_ids = invoices.id
        for record in self:
            valures_fac=len(record.invoice_ids)
            record.invoice_count = valures_fac
        for order in self:
            invoices = self.env['account.invoice']
            for line in order.order_line:
                invoices |= line.invoice_lines.mapped('invoice_id')
            order.invoice_ids = invoices
            order.invoice_count = len(invoices)

    @api.model
    def create(self,vals):
        if vals.get('requisition_id'):
            purchase_ids = self.env['purchase.order'].search([('requisition_id','=',vals.get('requisition_id'))])
            for po_id in purchase_ids:
                if vals.get('partner_id') == po_id.partner_id.id:
                    raise UserError(_('RFQ is available for this purchase agreement for the same vendor'))
        return super(PurchaseOrder, self).create(vals)

    @api.multi
    def write(self, vals):
        context = self._context # para saber que usuario esta en sesion
        current_uid = context.get('uid')
        user = self.env['res.users'].search([('id','=',current_uid)])
        group= self.env['res.groups'].search([('name','=','validacion_director'),('users','=',user.id)]) 
        # identifico que usuario esta en sesion y que si ese usuario pertenece al grupo de validacion director
        if vals.get('partner_id') or vals.get('requisition_id'):
            purchase_ids = self.env['purchase.order'].search([('requisition_id', '=', vals.get('requisition_id'))])
            for po_id in purchase_ids:
                if vals.get('partner_id') == po_id.partner_id.id:
                    raise UserError(_('RFQ is available for this purchase agreement for the same vendor'))
        print("imprimiendo vals de purchase") 
        print(vals)
        keys=vals.keys()
        values=vals.values()
        print(keys)
        print(values)
        dom=[]
        if (('state' in keys)& ('purchase' in values)): # pregunto si state esta en lso campos que han cambiado de estod y que si values esta purchase

            if(group): 
                print("Creando purchase:::::::::::::::")                  
                
                purchase_actual=super(PurchaseOrder, self).write(vals) #se crea la purchase order
                #self.invoice_count=1
                
                factura_obj = self.env['account.invoice']

                print("SE CREO FACTURA::::::::::")
                for line in self.order_line:
                    self.set_amortizacion_data(line)
                
                return purchase_actual
            else:
                print("creando purchase")   
                purchase_actual=super(PurchaseOrder, self).write(vals)           

                return purchase_actual
        return super(PurchaseOrder, self).write(vals)

    def set_amortizacion_data(self, linea):
        product = self.env['product.product'].browse(linea.product_id.id)
        contrato=product.categ_id.x_contrato
        x_anticipo=product.categ_id.x_anticipo
        x_retencion=product.categ_id.x_retencion
        porcentaje=100 #representa el 100% de toda la cantidad
        cost=linea.price_unit
        
        if contrato:
            costo_anticipo=(cost * x_anticipo)/porcentaje #se saca la cantidad del costo total menos el porentaje del anticipo
            retencion=(cost * x_retencion)/porcentaje # se saca el costo menos la retencion 
            cost=costo_anticipo-retencion 
            print(cost)       
            linea.price_unit=cost
            
            #####DATA AMORTIZACION
            linea.retencion_amortizacion=retencion*linea.product_qty

 
    @api.multi
    def compare_purchase_orders(self):
        context = dict(self._context or {})
        active_ids = context.get('active_ids', []) or []
        purchase_orders_id = self.env['purchase.order'].search([("id","in",active_ids)])
        vendor_list = []
        for rec in purchase_orders_id:
            if not rec.partner_id in vendor_list:
                vendor_list.append(rec.partner_id)
            else:                
                raise UserError(_('Same Vendors should not be selected, Please select different vendors for Purchase Comparison'))
       
        purchase_orders = self.env['purchase.order'].browse(self.ids)
        if len(purchase_orders) == 0:
            raise UserError(_('No RFQ available for compare. Please add some RFQ to compare'))
        purchase_orders = self.env['purchase.order'].search([('id', 'in', self.ids),('state','=', 'draft')])

        if not purchase_orders:
            raise UserError(_('All RFQs are processed. Please create new quotation'))
        base_url = '/' if self.env.context.get('relative_url') else self.env['ir.config_parameter'].get_param('web.base.url')

        list_id = False
        for record in purchase_orders:
            list_id = record.product_list_id
        if not list_id:
            redirect_url = "purchase_comparison_chart/purchase_comparison_product_list/po/%s" % (slugify(active_ids))
        else:
            redirect_url = "purchase_comparison_chart/purchase_comparison_product_list/%s" % (slugify(list_id.id))
        
        return {
            'type': 'ir.actions.act_url',
            'name': "Purchase Comparison Chart",
            'target': 'self',
            'url':redirect_url
        }
