# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class TipoGarantia(models.Model):
    _name = 'tipo.garantia'
    _description = 'Tipo garantia'
    
    name = fields.Char(
                       string="Tipo de garantía",
                       )
                       
                           
