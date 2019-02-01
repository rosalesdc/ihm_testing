# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class CalendarioEntrega(models.Model):
    
    _name = 'calendario.entrega'

    name = fields.Char(
                       string="Nombre")
                       
    fecha_agendada = fields.Date()
    hora_agendada = fields.Float()
    id_po_deliver = fields.Many2one(
                                    'stock.picking',
                                    string="Entrega"
                                    )
    

class StockPikingDeliver(models.Model):
    _inherit = 'stock.picking'
    
#    @api.multi
#    def _compute_meeting_count(self):
#        meeting_data = self.env['calendar.event'].read_group([('x_deliver_id', 'in', self.ids)], ['x_deliver_id'], ['x_deliver_id'])
#        mapped_data = {m['x_deliver_id'][0]: m['x_deliver_id'] for m in meeting_data}
#        for lead in self:
#            lead.meeting_count = mapped_data.get(lead.id, 0)                                   
    
    @api.multi
    def _compute_meeting_count(self):
        contador = 0
        for line in self.x_calendario_ids:
            contador += 1
            
        self.meeting_count=contador
        
        #self.importe_total_elementos = sum(line.importe for line in self.x_asignacion_ids)
        
    
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
            'default_x_deliver_id': self.id,
            'default_partner_id': self.partner_id.id,
            'default_partner_ids': partner_ids,
            #'default_team_id': self.team_id.id,
            'default_name': self.name,
        }
        return action
    
    x_calendario_ids = fields.One2many(
                                       'calendar.event', #modelo al que se hace referencia
                                       'x_deliver_id', #un campo de regreso
                                       string="Calendario entregas"
                                       )
    
    #LAMAR AQUI LA FUNCION PARA CONTAR LOS MEETINGS
    
    meeting_count = fields.Integer(string='# Meetings',
                                   readonly=True,
                                   compute='_compute_meeting_count',
                                   )                               
    

class CalendarEventDeliver(models.Model):
    _inherit = 'calendar.event'
    
    x_deliver_id = fields.Many2one(
                                   'stock.picking', #modelo al que se hace referencia
                                   string="Entrega"
                                   )