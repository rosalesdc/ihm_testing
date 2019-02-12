# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api
from odoo import fields
from odoo import models

class StockState(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection([
                             ('draft', 'Borrador'),
                             ('waiting', 'Esperando otra operacion'),
                             ('confirmed', 'En espera'),
                             ('assigned', 'En preparación'),
                             ('process', 'Liberado'),
                             ('done', 'Hecho'),
                             ('cancel', 'Cancelado'),
                             ], string='Status', compute='_compute_state',
                             copy=False, index=True, readonly=True, store=True, track_visibility='onchange',
                             help=" * Draft: not confirmed yet and will not be scheduled until confirmed.\n"
                             " * Waiting Another Operation: waiting for another move to proceed before it becomes automatically available (e.g. in Make-To-Order flows).\n"
                             " * Waiting: if it is not ready to be sent because the required products could not be reserved.\n"
                             " * Ready: products are reserved and ready to be sent. If the shipping policy is 'As soon as possible' this happens as soon as anything is reserved.\n"
                             " * Done: has been processed, can't be modified or cancelled anymore.\n"
                             " * Cancelled: has been cancelled, can't be confirmed anymore.")
                             
    @api.multi
    def set_state_assigned_picking(self): #
        self.ensure_one()
        self.write({'state': 'process'})
        for lines in self.move_lines:
            lines.product_id.estatus = "Liberado"
            
    @api.multi
    def set_state_done_picking(self): #
        
        for lines in self.move_lines:
            lines.product_id.estatus = "Entregado"
        
#        oportunidad = self.env['crm.lead'].search([('id_numero_referencia.name', '=', escritura.orden_venta_id.id_numero_referencia.name)], limit=1)
#        producto_inmueble = self.env['product.template'].search([('id', '=', oportunidad.id_producto_inmueble.id)], limit=1)
#        producto_inmueble.estatus="Escriturado"
        
        
        
    @api.multi
    @api.depends('state', 'is_locked')
    def _compute_show_validate(self):
        for picking in self:
            if not (picking.immediate_transfer) and picking.state == 'draft':
                picking.show_validate = False
            elif picking.state not in ('draft', 'waiting', 'confirmed', 'assigned', 'process') or not picking.is_locked:
                picking.show_validate = False
            else:
                picking.show_validate = True
                
                      
        
    @api.depends('move_type', 'move_lines.state', 'move_lines.picking_id')
    @api.one
    def _compute_state(self):
        ''' State of a picking depends on the state of its related stock.move
        - Draft: only used for "planned pickings"
        - Waiting: if the picking is not ready to be sent so if
          - (a) no quantity could be reserved at all or if
          - (b) some quantities could be reserved and the shipping policy is "deliver all at once"
        - Waiting another move: if the picking is waiting for another move
        - Ready: if the picking is ready to be sent so if:
          - (a) all quantities are reserved or if
          - (b) some quantities could be reserved and the shipping policy is "as soon as possible"
        - Done: if the picking is done.
        - Cancelled: if the picking is cancelled
        '''

        if not self.move_lines:
            self.state = 'draft'
        elif any(move.state == 'draft' for move in self.move_lines):  # TDE FIXME: should be all ?
            self.state = 'draft'
        elif all(move.state == 'cancel' for move in self.move_lines):
            self.state = 'cancel'
        elif all(move.state in ['cancel', 'done'] for move in self.move_lines):
            self.state = 'done'
        else:
            relevant_move_state = self.move_lines._get_relevant_state_among_moves()
            if relevant_move_state == 'partially_available':
                self.state = 'assigned'
            else:
                self.state = relevant_move_state
        
        if self.state is 'done':
            #Cambiar el estado del inmueble
            for lines in self.move_lines:
                print("Cambiando estados")
                #cambiando el estado desde las lineas
                #lines.product_id.estatus = "Entregado"
                
                #cambiando el estado buscando el registro
                producto_inmueble = self.env['product.template'].search([('id', '=', lines.product_id.id)], limit=1)
                producto_inmueble.estatus = "Entregado"            
        print("fin del metodo")

        