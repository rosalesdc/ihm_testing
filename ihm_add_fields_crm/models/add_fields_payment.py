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
                                           
    @api.multi
    def post(self):
        res = super(AddPaymentFields, self).post()

        #Checar si el pago tiene número de referencia
        if self.id_numero_referencia.name:
            print("CON referencia")
            monto_pago=self.amount
            if monto_pago>20000 and monto_pago<50000:
                oportunidad = self.env['crm.lead'].search([('id_numero_referencia', '=', self.id_numero_referencia.name)], limit=1)
                producto_inmueble=self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
                producto_inmueble.estatus='Apartado'
                print("Inmueble Apartado")
            if monto_pago>50000:
                oportunidad = self.env['crm.lead'].search([('id_numero_referencia', '=', self.id_numero_referencia.name)], limit=1)
                producto_inmueble=self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
                producto_inmueble.estatus='Vendido'
                print("Inmueble Vendido")
                
            
        else:
            print("SIN referencia")