# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class HelpDeskInherited(models.Model):
    _inherit = 'helpdesk.ticket'
    
    x_inmueble_id = fields.Many2one(
                                    'product.template', #nombre del modelo con el que se relaciona
                                    string="Inmueble"
                                    )
    x_detalle_id = fields.Many2one(
                                   'detalle.reparaciones', #nombre del modelo con el que se relaciona
                                   string="Detalle de reparaciones"
                                   )


class DetalleReparaciones(models.Model):
    _name = 'detalle.reparaciones'
    name = fields.Char(string="Detalle")
    categoria_falla_id = fields.Many2one(
                                        'categoria.falla',
                                        string="Categoría de Falla"
                                         )
                                         
    acta_reparaciones_id = fields.Many2one(
                                        'acta.reparaciones',
                                        string="Acta de reparaciones"
                                         )



class CategoriaFalla(models.Model):
    _name = 'categoria.falla'
    
    name = fields.Char(string="Categoría de falla")
    
class ActaReparaciones(models.Model):
    _name = 'acta.reparaciones'
    
    name = fields.Char(string="Acta de reparaciones")
    
