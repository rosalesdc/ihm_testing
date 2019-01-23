# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class SaleOrderMod(models.Model):
    _inherit = 'sale.order'
    
    opportunity_id = fields.Many2one(
                                     'crm.lead',
                                     string='Oportunidad',
                                     required=True,
                                     )

    x_id_numero_referencia = fields.Many2one(
                                             string='Número de Referencia',
                                             store=True,
                                             related='opportunity_id.id_numero_referencia',
                                             )
                                             
    pagos_ids = fields.Many2many(
                                'account.payment',
                                string="Pago",
                                store=True,
                                )
                                
#class PagosSaleOrders(models.Model):
#    _inherit='account.payment'
#    
#    
#    