# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class CampoRelacionProduct(models.Model):
    _inherit = 'crm.lead'
    
    id_producto_inmueble = fields.Many2one(
                                           'product.template',
                                           string="Inmueble asociado"
                                           )

    id_proyecto = fields.Many2one(
                                  'project.project',
                                  string="Proyecto asociado"
                                  )