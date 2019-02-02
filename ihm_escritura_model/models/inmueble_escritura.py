
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