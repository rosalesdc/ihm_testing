# -*- coding: utf-8 -*-
# Copyright YEAR(S), AUTHOR(S)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api
from odoo import fields
from odoo import models

class StockState(models.Model):
    _inherit = 'stock.picking'

    state = fields.Selection([
                             ('draft', 'Escriturado'),
                             ('waiting', 'Esperando otra operacion'),
                             ('confirmed', 'En preparación'),
                             ('assigned', 'Liberado'),
                             ('done', 'Entregado'),
                             ('cancel', 'Cancelado'),
                             ], string='Status', compute='_compute_state',
                             copy=False, index=True, readonly=True, store=True, track_visibility='onchange',
                             help=" * Draft: not confirmed yet and will not be scheduled until confirmed.\n"
                             " * Waiting Another Operation: waiting for another move to proceed before it becomes automatically available (e.g. in Make-To-Order flows).\n"
                             " * Waiting: if it is not ready to be sent because the required products could not be reserved.\n"
                             " * Ready: products are reserved and ready to be sent. If the shipping policy is 'As soon as possible' this happens as soon as anything is reserved.\n"
                             " * Done: has been processed, can't be modified or cancelled anymore.\n"
                             " * Cancelled: has been cancelled, can't be confirmed anymore.")

#    @api.multi
#    def set_state_assigned_picking(self): #
#        self.ensure_one()
#        self.write({'state': 'process'})
#        for lines in self.move_lines:
#            lines.product_id.estatus = "Liberado"

#    @api.multi
#    def set_state_done_picking(self): #
#
#        for lines in self.move_lines:
#            lines.product_id.estatus = "Entregado"

    @api.multi
    @api.depends('state')
    def _cambia_estatus(self):
        print("Cambiando estado")
        if self.state == "assigned":
            #Cambiar el estado del inmueble
            print("El estado de la orden es Preparado")
            for lines in self.move_lines:
                #cambiando el estado desde las lineas
                #lines.write({'estatus': 'Liberado'})

                #cambiando el estado buscando el registro
                producto_inmueble = self.env['product.product'].search([('id', '=', lines.product_id.id)], limit=1)
                #print("En for1 con " + producto_inmueble.name + " - " + producto_inmueble.estatus)
                if producto_inmueble.estatus == "Escriturado":
                    print("Cambiando -- Preparacion")
                    producto_inmueble.write({'estatus': 'Preparacion'})
                producto_inmueble2 = self.env['product.product'].search([('id', '=', lines.id)], limit=1)
                #print("Nueva variable: "+producto_inmueble2.estatus)

        if self.state == "done":
            #Cambiar el estado del inmueble
            print("El estado de la orden es Done")
            for lines in self.move_lines:
                #cambiando el estado desde las lineas
                #lines.write({'estatus': 'Liberado'})

                #cambiando el estado buscando el registro
                producto_inmueble = self.env['product.product'].search([('id', '=', lines.product_id.id)], limit=1)
                #print("En for2 con " + producto_inmueble.name + " - " + producto_inmueble.estatus)
                if producto_inmueble.estatus == "Preparacion":
                    print("Cambiando -- Entregado")
                    producto_inmueble.write({'estatus': 'Entregado'})
                producto_inmueble2 = self.env['product.product'].search([('id', '=', lines.product_id.id)], limit=1)
                #print("Nueva variable: "+producto_inmueble2.estatus)
#
        return "Cambiando"

    @api.model
    def _default_estado_id(self):
        return self.env['estatus.model'].search([('id', '=', '9')], limit=1)
 

    cambia_estatus_inmueble = fields.Char(compute='_cambia_estatus')

    estado_id = fields.Many2one(
                                     'estatus.model',
                                     string="Estatus",
                                     default=_default_estado_id
                                     )
