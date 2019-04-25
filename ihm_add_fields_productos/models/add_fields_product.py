# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError
import smtplib

class AddProductFields(models.Model):
    _inherit = 'product.template'
    name = fields.Char('Name', index=True, required=True, translate=False)

    #Antes de crear un producto checa que el usuario no esté restringido
    @api.model
    def create(self, vals):
        producto_creado=super(AddProductFields, self).create(vals)
        if producto_creado.is_group_restr == True:
            raise ValidationError('Usuario actual no puede crear inmuebles')
        else: return producto_creado
        
    #Antes de actualizar el producto se verifica si el usuario es administrador
    @api.multi
    def write(self, vals):
        if self.es_inmueble == True and self.is_group_admin == False:
            raise ValidationError('Usuario actual no puede actualizar inmuebles')
        else:
            return super(AddProductFields, self).write(vals)
    #Antes de eliminar el producto se verifica si el usuario es administrador
    @api.multi
    def unlink(self):
        if self.es_inmueble == True and self.is_group_admin == False:
            raise ValidationError('Usuario actual no puede eliminar inmuebles')
        else:
            return super(AddProductFields, self).unlink()
        
    @api.one
    @api.depends('x_asignacion_ids.importe')
    def _compute_total_elementos(self):
        self.importe_total_elementos = sum(line.importe for line in self.x_asignacion_ids)
        
    @api.one
    def asignar_precio_inmueble(self):
        precio_calculado = float(self.importe_total_elementos)
        self.write({'list_price': precio_calculado})
        
    @api.model
    def get_default_estatus(self):
        default_estatus = 'Disponible'
        return default_estatus
    
    @api.one
    @api.depends('estatus')
    def _compute_copy_estatus(self):
        if self.estatus != False:
            if self.estatus == "Disponible":
                self.estatus_ordenado = "01-Disponible"
            elif self.estatus == "Apartado":
                self.estatus_ordenado = "02-Apartado"
            elif self.estatus == "Vendido":
                self.estatus_ordenado = "03-Vendido"
            elif self.estatus == "Escriturado":
                self.estatus_ordenado = "04-Escriturado"
            elif self.estatus == "Preparacion":
                self.estatus_ordenado = "05-Liberado"
            elif self.estatus == "Entregado":
                self.estatus_ordenado = "06-Entregado"
    
    @api.one
    @api.model
    @api.depends('sale_order')
    def _obtener_referencia(self):        
        orden = self.env['sale.order'].search([('id', '=', self.sale_order.id)])
        #self.xreferencia=orden.name 
        self.xreferencia = orden.id_numero_referencia.name
                
    #Funcion que busca al usuario en el grupo de administradores
    @api.one
    def _compute_is_group_admin(self):
        self.is_group_admin = self.env['res.users'].has_group('ihm_ocultar_validar.group_director')
        
    #Funcion que busca que el usuario no pertenezca al campo que puede editar/crear productos
    @api.one
    def _compute_is_group_restringido(self):
        self.is_group_restr = self.env['res.users'].has_group('ihm_ocultar_validar.group_no_editarcrear')
       
    #Campo para revisar si el usuario actual es un administrador
    is_group_admin = fields.Boolean(
                                    string='Is Admin',
                                    compute="_compute_is_group_admin",
                                    )
    is_group_restr = fields.Boolean(
                                    string='Is Restringido',
                                    compute="_compute_is_group_restringido",
                                    )
       
    #características para los productos que son inmuebles y su proyecto relacionado
    es_inmueble = fields.Boolean(string="Es un inmueble")
    
    caracteristicas = fields.Text(string="Características")
    numero = fields.Char(string="Número")
    estatus = fields.Selection(
                               selection=[
                               ('Disponible', '01 Disponible'),
                               ('Apartado', '02 Apartado'),
                               ('Vendido', '03 Vendido'),
                               ('Escriturado', '04 Escriturado'),
                               ('Preparacion', '05 Liberado'),
                               ('Entregado', '06 Entregado'),
                               ],
                               string="Estatus",
                               copy=False,
                               readonly=True,
                               default=get_default_estatus,
                               )
    estatus_ordenado = fields.Char(string="Estatus ordenado",
                                   readonly=True, 
                                   store=True,
                                   compute='_compute_copy_estatus', )
                                
    x_proyecto_id = fields.Many2one('project.project', string='Proyecto')
    
    x_asignacion_ids = fields.One2many(
                                       'asignacion.elementos', #modelo al que se hace referencia
                                       'inmueble_id', #un campo de regreso
                                       string="Asignacion elementos"
                                       )
                                       
#CAMPO PARA EL CALCULO DE TOTAL DE LOS ELEMENTOS
    importe_total_elementos = fields.Float(string='Importe total elementos',
                                           #store=True, 
                                           readonly=True, 
                                           compute='_compute_total_elementos',
                                           )
        
    oportunidades_ids = fields.One2many(
                                        'crm.lead', #modelo al que se hace referencia
                                        'id_producto_inmueble', #un campo de regreso
                                        string="Oportunidad"
                                        )#
                                        
    cantidad_enganche = fields.Float(
                                     string="Cantidad Contrato"
                                     )
    garantia_id = fields.Many2one(
                                  'tipo.garantia',
                                  string="Tipo de garantia"
                                  )
    sale_order = fields.Many2one(
                                 'sale.order',
                                 copy=False,
                                 string="Orden de venta del"
                                 )
                                 
    xreferencia = fields.Char(
                              string='Referencia',
                              #store=True,
                              compute='_obtener_referencia',
                              )
    
#https://fundamentos-de-desarrollo-en-odoo.readthedocs.io/es/latest/capitulos/modelos-estructura-datos-aplicacion.html
