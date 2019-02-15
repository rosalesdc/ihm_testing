# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class EstatusModel(models.Model):
    _name = 'estatus.model'

    name = fields.Char(string="Estatus")
