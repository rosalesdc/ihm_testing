# -*- coding: utf-8 -*-

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
