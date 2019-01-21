# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models
from odoo import api

class ElementosPrecio(models.Model):
    _name = 'elementos.precio'
    
    name = fields.Char(
                       string="Nombre"
                       )
    uom = fields.Many2one(
                          'uom.uom', #nombre del modelo con el que se relaciona
                          string="Unidad de medida"
                          )
    precio_venta = fields.Float(
                                string="Precio de Venta",
                                default=0.0
                                )
    proyecto_id = fields.Many2one(
                                 'project.project',
                                 string="Proyecto"
                                 )