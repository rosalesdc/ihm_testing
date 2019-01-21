# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class ProyectoElementos(models.Model):
    _inherit = 'project.project'
    x_elementos_ids = fields.One2many(
                                'elementos.precio', #modelo al que se hace referencia
                                'proyecto_id', #un campo de regreso
		string="Elementos de Precio"
		)