# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Teachers(models.Model):
    _name = 'ejercicios01.teachers'

    name = fields.Char()