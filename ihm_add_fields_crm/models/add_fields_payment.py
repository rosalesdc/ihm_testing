# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class AddPaymentFields(models.Model):
    _inherit = 'account.payment'

    sale_orders_ids = fields.Many2many(
                                       'sale.order',
                                       string="Ordenes Venta",
                                       store=True,
                                       )

    x_id_nreferencia = fields.Char(
                                       string='Número de Referencia',
                                       
                                       
                                       )