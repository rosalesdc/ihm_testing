# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class FacturaAmortizacion(models.Model):
    _inherit = 'account.payment'

    
    x_cuenta_analitica_id = fields.Many2one('account.analytic.account', compute="_compute_analitica", string='Cuenta Analitica')
    
    @api.depends('invoice_ids')
    def _compute_analitica(self):
        print("EN FUNCION:::::::::::::::::::::")
        for record in self.invoice_ids[0]:
            orden=record.purchase_id
            self.x_cuenta_analitica_id=orden.x_cuenta_analitica_id