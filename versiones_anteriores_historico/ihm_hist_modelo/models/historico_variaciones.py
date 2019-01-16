
# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models
from odoo.addons import decimal_precision as dp

class HistoricoVariaciones(models.Model): 
    _name = 'historico.variaciones'
    
    date_order = fields.Datetime(
                                string="Fecha de pedido"
                                )
    product_id = fields.Many2one(
                                 'product.product', #nombre del modelo con el que se relaciona
                                 string="Producto",
                                 change_default=True, required=True)
    
    price_unit = fields.Float('Cost', digits=dp.get_precision('Product Price'))
    partner_id = fields.Many2one('res.partner',
                                 string='Partner',
                                 required=True,
                                 store=True)
    #x_precio_nuevo = fields.Boolean(default=True)
