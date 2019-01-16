# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class AddProductFields(models.Model):
    _inherit = 'product.template'
    
    es_inmueble=fields.Boolean(string="Es un inmueble")
    caracteristicas=fields.Char(string="Características")
    metros_cuadrados=fields.Float(string="Metros cuadrados")
    nivel=fields.Char(string="Nivel (piso)")
    x_proyecto_id = fields.Many2one('project.project',string='Proyecto')