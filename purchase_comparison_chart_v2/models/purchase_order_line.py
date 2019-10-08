

from odoo import fields
from odoo import models

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order.line'
    
    retencion_amortizacion = fields.Float(string="Retención para amortización")