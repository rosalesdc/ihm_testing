# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'
    
    x_venta_escritura_id = fields.Many2one(
                                       'venta.escrituras', #nombre del modelo con el que se relaciona
                                       string="Escrituras"
                                       )