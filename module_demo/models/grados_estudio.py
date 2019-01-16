# -*- coding: utf-8 -*-
from odoo import models,fields

class GradosEstudio(models.Model):
	_name='personas.grados_estudio'

	name=fields.Char(
		string="Nivel de estudios",
		required=True,
		)
	anios=fields.Integer(
		string="Años  de estudio"
		)