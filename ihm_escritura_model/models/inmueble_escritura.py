# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class InmuebleEscritura(models.Model): 
    _name = 'inmueble.escritura'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(string="Número de Escritura")
    notaria = fields.Char(string="Notaría")
    fecha = fields.Datetime(
                            string="Fecha de Escritura"
                            )
    
    orden_venta_id = fields.Many2one(
                                     'sale.order',
                                     string="Orden"
                                     )
    
    @api.model
    def create(self, vals):
        #CAMBIA EL ESTATUS DEL INMUEBLE A ESCRITURADO
        print("CREATING VALUES:::::::::::::::::::::::::")
        escritura = super(InmuebleEscritura, self).create(vals)
        oportunidad = self.env['crm.lead'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)
        producto_inmueble = self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
        producto_inmueble.estatus="Escriturado"
        return escritura
        
