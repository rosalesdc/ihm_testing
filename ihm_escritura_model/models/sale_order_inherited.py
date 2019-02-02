# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    x_inmueble_escritura_id = fields.Many2many(
                                          'venta.escrituras',
                                          string="Escritura/Contrato"
                                          )
    
#    x_venta_escritura_ids = fields.One2many(
#                                'venta.escrituras', #modelo al que se hace referencia
#                                'orden_id', #un campo de regreso
#                                string="Escritura/Contrato"
#                                )
    
#    x_venta_escritura_id = fields.Many2one(
#                                       'venta.escrituras', #nombre del modelo con el que se relaciona
#                                       string="Escritura/Contrato"
#                                       )