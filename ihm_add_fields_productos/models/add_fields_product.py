# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class AddProductFields(models.Model):
    _inherit = 'product.template'
    
    #características para los productos que son inmuebles y su proyecto relacionado
    es_inmueble = fields.Boolean(string="Es un inmueble")
    caracteristicas = fields.Char(string="Características")
    metros_cuadrados = fields.Float(string="Metros cuadrados")
    nivel = fields.Char(string="Nivel (piso)")
    x_proyecto_id = fields.Many2one('project.project', string='Proyecto')
    
    #Campo para relación con información sobre  UOM,QTY y Cantidad monetaria para inmuebles
    x_cantidades_inmueble = fields.One2many(
                                            'cantidades.inmueble', #modelo al que se hace referencia
                                            'inmueble_id', #un campo de regreso
                                            string="Elementos de cantidades"
		)