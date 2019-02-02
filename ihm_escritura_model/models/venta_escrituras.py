# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class VentaEscrituras(models.Model):
    _name = 'venta.escrituras'
#    _inherit = ['mail.thread']
#    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    name = fields.Char(
                       string="Numero Escrituras",
                       )
    notaria = fields.Char(
                          string="Notaría",
                          )
    fecha_escritura = fields.Date(
                                  string="Fecha"
                                  )

#    orden_id = fields.Many2one(
#                                 'sale.order',
#                                 string="Orden"
#                                 )
                
#    attachment = fields.Binary(string="Attachment",)    
#    store_fname = fields.Char(string="File Name")