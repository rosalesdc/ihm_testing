# -*- coding: utf-8 -*-

from odoo import models,fields

class NombreCuentasEmail(models.Model):
	_name='personas.nombre_cuentas_email'

	name=fields.Char(
		string="Dominio",
		required=True
		)
	dominio_publico=fields.Boolean(
		string="El dominio es público?"
		)