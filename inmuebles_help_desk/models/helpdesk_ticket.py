# -*- coding: utf-8 -*-

from odoo import models, fields, api

class InmuebleFillAutomation(models.Model):
    _inherit = 'helpdesk.ticket'

    inmuebles_id = fields.Many2one('inmuebles.helpdesk', string='Inmuebles Asociados')