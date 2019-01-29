# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class AddProductFields(models.Model):
    _inherit = 'product.template'
    
    #FUNCION PARA CALCULO DE ELEMENTOS
#    @api.one
#    @api.depends('invoice_line_ids.price_subtotal')
#    def _compute_total_elementos(self):
#        self.importe_total_elementos = sum(line.importe for line in self.x_asignacion_ids)

    #Para relacionar los inmuebles de tipo "bien adicional" con un inmueble "normal"
    _parent_store = True
    parent_id     = fields.Many2one('product.template', string="Inmueble relacionado")
    parent_left   = fields.Integer('Parent Left', index=True)
    parent_right  = fields.Integer('Parent  Right', index=True)
    #child_ids = fields.One2many('product.tempĺate', 'parent_id')
    
    #características para los productos que son inmuebles y su proyecto relacionado
    es_inmueble = fields.Boolean(string="Es un inmueble")
    es_bien_adicional = fields.Boolean(string="Es un bien adicional")
    tipo_bien_adicional = fields.Selection(
                                           selection=[
                                           ('Cajon de Estacionamiento', 'Cajón de Estacionamiento'),
                                           ('Bodega', 'Bodega'),
                                           ],
                                           string="Tipo de bien adicional",
                                           default='Bodega',
                                           )
    caracteristicas = fields.Text(string="Características")
    numero = fields.Char(string="Número")
    estatus = fields.Selection(
                               selection=[
                               ('Disponible', 'Disponible'),
                               ('Apartado', 'Apartado'),
                               ('Vendido', 'Entregado'),
                               ('Entregado', 'Entregado'),
                               ],
                               string="Estatus"
                               )
    x_proyecto_id = fields.Many2one('project.project', string='Proyecto')
    
    x_asignacion_ids = fields.One2many(
                                       'asignacion.elementos', #modelo al que se hace referencia
                                       'inmueble_id', #un campo de regreso
                                       string="Asignacion elementos"
                                       )
#CAMPO PARA EL CALCULO DE TOTAL DE LOS ELEMENTOS
#    importe_total_elementos = fields.Float(string='Importe total elementos',
#                                           store=True, readonly=True, compute='_compute_total_elementos')
        
    oportunidades_ids = fields.One2many(
                                        'crm.lead', #modelo al que se hace referencia
                                        'id_producto_inmueble', #un campo de regreso
                                        string="Oportunidad"
                                        )#
                                            

#https://fundamentos-de-desarrollo-en-odoo.readthedocs.io/es/latest/capitulos/modelos-estructura-datos-aplicacion.html