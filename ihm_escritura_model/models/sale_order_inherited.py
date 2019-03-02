#-*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    escritura=fields.Char(string="Escritura")