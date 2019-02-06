# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class CamposProyecto(models.Model):
    _inherit = 'project.project'
    
    cantidad_apartado = fields.Float(
                                     string="Cantidad Apartado"
                                     )
                                     
    equipo_entrega = fields.Many2many(
                                      'res.partner',
                                      string="Equipo de entrega"
                                      )

