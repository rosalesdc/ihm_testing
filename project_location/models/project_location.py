# -*- coding: utf-8 -*-

from odoo import fields, models, api

class projectLocation(models.Model):
	_inherit = 'project.project'

	location_ids = fields.One2many('stock.location','project_id',string='Ubicaciones')

	@api.multi
	def get_main_location(self, name, usage):
		self.ensure_one()
		return self.location_ids.filtered(
			lambda l: l.name == name and l.usage == usage)

	def _create_main_partner_location(self):
		parent = self.env['stock.location'].search(['|','|','|',
			('name', '=', 'Azotea'),('name', '=', 'Tercer Piso'),
			('name', '=', 'Laboratorio'),('name','=','Clientes')])
		location_out = self.env.ref('stock.stock_location_customers').id
		if parent:
			for record in parent:
				if record.usage == 'customer':
					location = (
					self.get_main_location(record.name,'customer') or
					self._create_main_location(record.name,'customer',location_out))
				if record.usage == 'internal':
					location = (
					self.get_main_location(record.name,'internal') or
					self._create_main_location(record.name,'internal',record.id))

	@api.multi
	def _create_main_location(self, name, usage, parent):
		self.ensure_one()

		#parent = (self.get_main_location(name,usage))

		return self.env['stock.location'].create({
			'name': self.name,
			'usage': usage,
			'location_id': parent,
		})

	@api.model
	def create(self, vals):
		partner = super(projectLocation, self).create(vals)

		if vals.get('name', False):
			partner._create_main_partner_location()

		return partner

	@api.multi
	def write(self, vals):
		if vals.get('name'):
			for partner in self:
				locations = partner.location_ids.filtered(
					lambda l: l.name == partner.name)
				locations.write({'name': vals.get('name')})

		res = super(projectLocation, self).write(vals)
		return res

class locationProject(models.Model):
	_inherit = 'stock.location'

	project_id = fields.Many2one('project.project',string='Proyecto')