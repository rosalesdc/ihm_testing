# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class CamposResPartner(models.Model):
    _inherit = 'res.partner'
    
    id_nacionalidad = fields.Many2one(
                                      'partner.nacionalidad',
                                      string="Nacionalidad"
                                      )
    id_identificacion = fields.Many2one (
                                         'partner.identificacion',
                                         string="Identificación"
                                         )
    lugar_origen = fields.Char(
                               string="Lugar de origen"
                               )
    fecha_nacimiento = fields.Date()
    id_ocupacion = fields.Many2one(
                                   'partner.ocupacion',
                                   string="Ocupación"
                                   )
    antiguedad_en_empresa = fields.Char(string="Antigüedad en la empresa")
  
     #ESTOS DOS METODOS SE REEMPLAZAN CON UN ARCHIVO XML (DATA) PARA LA CREACION DE LA ETIQUETA ASESOR DE VENTA
#    @api.model
#    def tag_contac_create(self):
#        etiqueta = self.env['res.partner.category'].search_count([('name', '=','Asesor de Ventas')])
#        if etiqueta == 0:
#            vals={'name':'Asesor de Ventas'}
#            self.env['res.partner.category'].create(vals)
#        
#    @api.model
#    def create(self, vals):
#        contacto = super(CamposResPartner, self).create(vals)
#        self.tag_contac_create()
#        return contacto


class PartnerNacionalidad(models.Model):
    _name = 'partner.nacionalidad'
    name = fields.Char(
                       string="Nacionalidad",
                       )
                               
class PartnerIdentificacion(models.Model):
    _name = 'partner.identificacion'
    name = fields.Char(
                       string="Identificación",
                       )
                               
class PartnerOcupacion(models.Model):
    _name = 'partner.ocupacion'
    name = fields.Char(
                       string="Ocupación",
                       )
