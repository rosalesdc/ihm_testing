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
                             ('confirmed', 'Confirmado'),
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
       # if self.state=="confirmed":
       #     print("El estado de la orden es Confirmed")
       #     self.write({'estado_id': '8'}) # 8 ahora es el primer estado
        
        if self.state == "assigned":
            #Cambiar el estado del inmueble
            print("El estado de la orden es Assigned")
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
                
            #cambia el subestado
            
            if (self.estado_id.id==1 or self.estado_id.id==7): #EN IHM es 1 o 7, se le quitó el estado 8 de aqui por los que modificó odooBot
                print("cambia estado entrega")
                self.write({'estado_id': '2'}) # EN IHM es 2
            else:
                print("no cambia estado entrega")
                

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
            #cambia el subestado
            self.write({'estado_id': '7'}) #EN IHM ES 7
        return "Cambiando"

    @api.model
    def _default_estado_id(self):
        return self.env['estatus.model'].search([('id', '=', '8')], limit=1) #EN IHM ES 1


    cambia_estatus_inmueble = fields.Char(compute='_cambia_estatus')

    estado_id = fields.Many2one(
                                     'estatus.model',
                                     string="Estatus",
                                     default=_default_estado_id
                                     )
                                     
    estado_select = fields.Selection(
                             selection=[
                             ('liberado_cita', '-Liberado con cita'),
                             ('liberado_acta', '-Liberado con Acta Firmada'),
                             ('liberado_ticket', '-Liberado con ticket de detalles'),
                             ('no_presento', '-No se presentó a la cita'),
                             ],
                             default='liberado_cita',
                             String='Modificación de subestatus'
                             )

    productos_related = fields.Char(string='Productos',
                        related='sale_id.productos_reporte')
                        
    fecha_related = fields.Datetime(string='Productos',
                        related='sale_id.x_fecha_escritura')
                        
    
    def establecer_estado_id(self):
        self.env.cr.commit()
        if self.estado_select == 'liberado_cita':
            self.estado_id = '3'
        elif self.estado_select == 'liberado_acta':
            self.estado_id = '4'
        elif self.estado_select == 'liberado_ticket':
            self.estado_id = '5'
        elif self.estado_select == 'no_presento':
            self.estado_id = '6'
