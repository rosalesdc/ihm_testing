# -*- coding: utf-8 -*-

from odoo import fields, models, api

class poCuentaAnalitica(models.Model):
    _inherit = 'purchase.order'
    
    product_list_id = fields.Many2one('product.list',string='Product List')
