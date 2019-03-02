# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class AddPaymentFields(models.Model):
    _inherit = 'account.payment'
        

    sale_orders_ids = fields.Many2many(
                                       'sale.order',
                                       string="Ordenes Venta",
                                       store=True,
                                       )
                                       
    id_numero_referencia = fields.Many2one(
                                           'numero.referencia',
                                           string="Número de Referencia"
                                           )
    reportado = fields.Boolean(string="Reportado")
                                         
    @api.multi
    def post(self):
        res = super(AddPaymentFields, self).post()
        #Checar si el pago tiene número de referencia
        if self.id_numero_referencia.name:
            print("CON referencia")
            
            pagos=self.env['account.payment'].search([('id_numero_referencia', '=', self.id_numero_referencia.name),('state','=', 'posted')])
            oportunidad = self.env['crm.lead'].search([('id_numero_referencia', '=', self.id_numero_referencia.name)], limit=1)
            
            so=self.env['sale.order'].search([('id_numero_referencia', '=', self.id_numero_referencia.name)], limit=1)
            
            
            producto_inmueble=self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
            proyecto=self.env['project.project'].search([('id', '=', producto_inmueble.x_proyecto_id.id)], limit=1)
            
            if not pagos:
                print("No hay hay registros de pagos validados")
            monto_actual=0
            
            
            for montos in pagos:
                monto_actual+=montos.amount
                print(self.id_numero_referencia.name)
                print(monto_actual)
                print(self.partner_id.id)
                print("-------------")
                
            
            
            if (monto_actual>=proyecto.cantidad_apartado) and (monto_actual<=producto_inmueble.cantidad_enganche):
                #producto_inmueble.estatus='Apartado'
                print("Cantidad apartado alcanzado")
                for lines in so.order_line:
                    print(lines.product_id.estatus)
                    if lines.product_id.estatus == "Disponible":
                        print("Cambiando -- Apartado")
                        lines.product_id.write({'estatus': 'Apartado'})
                        print("Inmueble Apartado")
                
                
            if monto_actual>=producto_inmueble.cantidad_enganche:
                print("Cantidad vendido alcanzado")
                for lines in so.order_line:
                    print(lines.product_id.estatus)
                    if (lines.product_id.estatus == "Disponible") or (lines.product_id.estatus == "Apartado"):
                        print("Cambiando -- Vendido")
                        lines.product_id.write({'estatus': 'Vendido'})
                        print("Inmueble Vendido")
                
        else:
            print("SIN referencia")
                                           
#    @api.multi
#    def post(self):
#        res = super(AddPaymentFields, self).post()
#
#        #Checar si el pago tiene número de referencia
#        if self.id_numero_referencia.name:
#            print("CON referencia")
#            monto_pago=self.amount
#            if monto_pago>20000 and monto_pago<50000:
#                oportunidad = self.env['crm.lead'].search([('id_numero_referencia', '=', self.id_numero_referencia.name)], limit=1)
#                producto_inmueble=self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
#                producto_inmueble.estatus='Apartado'
#                print("Inmueble Apartado")
#            if monto_pago>50000:
#                oportunidad = self.env['crm.lead'].search([('id_numero_referencia', '=', self.id_numero_referencia.name)], limit=1)
#                producto_inmueble=self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
#                producto_inmueble.estatus='Vendido'
#                print("Inmueble Vendido")
#        else:
#            print("SIN referencia")