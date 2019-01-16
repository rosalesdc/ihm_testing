# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class VentaEscrituras(models.Model):
    _name = 'venta.escrituras'
    
    name = fields.Char(
                       string="Numero Escrituras",
                       )
    notaria = fields.Char(
                          string="Notaría",
                          )
    fecha_escritura = fields.Date(
                                  string="Fecha"
                                  )