# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class LineasCuentaAnalitica(models.Model):
    _inherit = 'purchase.order.line'
    
    account_analytic_id = fields.Many2one(string='Cuenta Analítica',
                        store=True, 
                        related='order_id.x_cuenta_analitica_id')
#