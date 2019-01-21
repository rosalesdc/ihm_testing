# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class CantidadesInmueble(models.Model):
    _name = 'cantidades.inmueble'

    name = fields.Char(
                         string="Nombre",
                         default="No name"
                         )
    uom = fields.Many2one(
                          'uom.uom', #nombre del modelo con el que se relaciona
                          string="Unidad de medida"
                          )
    cantidad = fields.Float(
                            string="Qty",
                            default=0.0
                            )
    cantidad_moneda = fields.Float(
                            string="Cantidad $",
                            default=0.0
                            )
                                
    inmueble_id = fields.Many2one(
                                  'product.template',
                                  string="Inmueble"
                                  )