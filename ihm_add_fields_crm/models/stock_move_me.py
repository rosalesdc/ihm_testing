# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class StockMoveMe(models.Model):
    _inherit = 'stock.picking'
    
    
    @api.model
    def create(self, vals):
        #self.ensure_one()
        res = super(StockMoveMe, self).create(vals)
        orden = res.env['sale.order'].search([('picking_ids', '=', res.sale_id.id)], limit=1)
        print("id_orden")
        print(orden.name)
        proyecto=self.env['project.project'].search([('id', '=', orden.id_proyecto.id)], limit=1)
        print("proyecto___default")
        #print(proyecto.name)
        res.write({'id_proyecto': proyecto.id})
        
#        for record in res:
#            print(record.id_asesor_ventas.name)
#            record.nombre_asesor = record.id_asesor_ventas.name
#            print(record.nombre_asesor)
        return res
    
    @api.model
    def _default_id_proyecto(self):
        orden = self.env['sale.order'].search([('id', '=', self.sale_id.id)], limit=1)
        print(orden.name)
        proyecto=self.env['project.project'].search([('id', '=', orden.id_proyecto.id)], limit=1)
        print("proyecto___default")
        #print(proyecto.name)
        return self.env['project.project'].search([('id', '=', orden.id_proyecto.id)], limit=1)
    
    id_proyecto = fields.Many2one(
                                  'project.project',
                                  string="Proyecto asociado",
                                  #default=_default_id_proyecto,
                                  #compute=_default_id_proyecto,
                                  #copy=False, index=True, readonly=True, store=True, track_visibility='onchange',
                                  )

    
