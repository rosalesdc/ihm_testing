# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class FacturaAmortizacion(models.Model):
    _inherit = 'account.payment'

    
    x_cuenta_analitica_id = fields.Many2one('account.analytic.account', compute="_compute_analitica", string='Cuenta Analitica')
    x_categoria_id = fields.Many2one('product.category', string='Contrato (categoria)')
    
    @api.depends('invoice_ids')
    def _compute_analitica(self):
        print("EN FUNCION:::::::::::::::::::::")
        if self.invoice_ids:
            for record in self.invoice_ids[0]:
                orden=record.purchase_id
                self.x_cuenta_analitica_id=orden.x_cuenta_analitica_id
                #if record.invoice_line_ids[0].product_id.categ_id.x_contrato == True: #Por el momento no hay otro lugar para tomar categoria
                    #self.x_categoria_id = record.invoice_line_ids[0].product_id.categ_id.id

    @api.model
    def create(self, vals):
        pago=super(FacturaAmortizacion, self).create(vals)
        if self.invoice_ids:
            for record in pago.invoice_ids[0]:
                if record.invoice_line_ids[0].product_id.categ_id.x_contrato == True: #Por el momento no hay otro lugar para tomar categoria
                    pago.x_categoria_id = record.invoice_line_ids[0].product_id.categ_id.id
                    print("PAGO RELACIONADO A CONTRATO")
        return pago