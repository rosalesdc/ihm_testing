# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class AsignacionElementos(models.Model):
    _name = 'asignacion.elementos'
    
    @api.onchange('cantidad','elemento_precio_unitario')
    def _compute_importe(self):
        for record in self:
            self.importe = self.cantidad*self.elemento_precio_unitario

    name = fields.Char(
                       string="Nombre",
                       default="No name"
                       )
    elemento_id = fields.Many2one(
                                  'elementos.precio', #nombre del modelo con el que se relaciona
                                  string="Elemento de precio"
                                  )
                                  
    elemento_precio_unitario= fields.Float(string='Precio unitario elemento',
                        store=True, 
                        related='elemento_id.precio_unitario')
    
    inmueble_id = fields.Many2one(
                                  'product.template',
                                  string="Inmueble"
                                  )
    cantidad = fields.Float(
                           string="Cantidad",
                           default=0.0
                           )
    importe = fields.Float(
                           string="Importe",
                           default=0.0,
                           readonly=True,
                           )
                           
    
