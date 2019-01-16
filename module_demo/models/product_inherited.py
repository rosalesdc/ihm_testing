# -*- coding: utf-8 -*-
# Agregar depencia antes al manifest, en depends['']

from odoo import fields,models

class ProductInherited(models.Model):
	_inherit='product.template'

	x_mi_campo=fields.Char(
		string="Mi campo de prueba"
		)