# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class HelpDeskCalendar(models.Model):
    _inherit = 'helpdesk.ticket'
    
    @api.multi
    def _compute_meeting_count(self):
        contador = 0
        for line in self.x_calendario_ids:
            contador += 1
        self.meeting_count=contador
    
    @api.multi
    def action_schedule_meeting(self):
        """ Open meeting's calendar view to schedule meeting on current opportunity.
            :return dict: dictionary value for created Meeting view
        """
        self.ensure_one()
        action = self.env.ref('calendar.action_calendar_event').read()[0]
        partner_ids = self.env.user.partner_id.ids
        if self.partner_id:
            partner_ids.append(self.partner_id.id)
        action['context'] = {
            'default_x_ticket_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_partner_ids': partner_ids,
            #'default_team_id': self.team_id.id,
            'default_name': self.name,
        }
        return action
    
    x_calendario_ids = fields.One2many(
                                       'calendar.event', #modelo al que se hace referencia
                                       'x_ticket_id', #un campo de regreso
                                       string="Calendario tickets"
                                       )
    
    #LAMAR AQUI LA FUNCION PARA CONTAR LOS MEETINGS
    
    meeting_count = fields.Integer(string='# Meetings',
                                   readonly=True,
                                   compute='_compute_meeting_count',
                                   )                               
    

class CalendarEventTicket(models.Model):
    _inherit = 'calendar.event'
    
    x_ticket_id = fields.Many2one(
                                   'helpdesk.ticket',
                                   string="Ticket"
                                   )