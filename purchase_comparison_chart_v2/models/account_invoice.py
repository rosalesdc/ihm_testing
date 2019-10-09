# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models


class FacturaAmortizacion(models.Model):
    _inherit = 'account.invoice'
    
    @api.multi
    def action_invoice_open(self):
        print ("En ACTION INVOICE_OPEN==")
        if self.state == 'draft' and self.type == 'in_invoice':
            #orden = self.env['purchase.order'].search([('name', '=', self.origin)], limit=1)
            orden = self.env['purchase.order'].search([('id', '=', self.purchase_id.id)], limit=1)
            retencion_total = 0
            categoria = orden.order_line[0].product_id.categ_id
            for line in orden.order_line:
                if line.retencion_amortizacion:
                    retencion_total += line.retencion_amortizacion
            if retencion_total != 0:
                amortizacion_obj = self.env['amortizacion.reporte']
                amortizacion_data = {'name':"Test",  'purchase_order_id': orden.id,'account_invoice_id': self.id,'cantidad_descontada':retencion_total,'categoria_id':categoria.id}
                amoritzacion_crear = amortizacion_obj.create(amortizacion_data)
        return super(FacturaAmortizacion, self).action_invoice_open()