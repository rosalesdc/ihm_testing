# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class AsignacionElementos(models.Model):
    _name = 'asignacion.elementos'
    
    @api.onchange('cantidad','elemento_precio_unitario')
    def _compute_importe(self):
        for record in self:
            #record.importe = self.cantidad*record.elemento_precio_unitario
            record.importe = record.cantidad*record.elemento_precio_unitario

    name = fields.Char(
                       string="Nombre",
                       default="No name"
                       )
                       
    elemento_id = fields.Many2one(
                                  'elementos.precio', #nombre del modelo con el que se relaciona
                                  string="Elemento de precio"
                                  )

    #CAMPOS RELATED PARA OBTENER VALORES                              
    elemento_precio_unitario= fields.Float(string='Precio unitario elemento',
                        store=True, 
                        related='elemento_id.precio_unitario')
    elemento_proyecto_id= fields.Many2one(string='Proyecto',
                        store=True, 
                        related='elemento_id.proyecto_id')                    
    #CAMPOS RELATED PARA OBTENER VALORES

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
                           store=False,
                           compute='_compute_importe',
                           )
                           