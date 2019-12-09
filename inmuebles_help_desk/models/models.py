# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError

class InmueblesHelpDesk(models.Model):
    _name = 'inmuebles.helpdesk'
    _description = 'Módulo para asociar cliente e inmueble.'

    name = fields.Char(string='Inmuebles', compute='get_name') 

    partner_id = fields.Many2one('res.partner', string="Cliente")
    product_id = fields.Many2one('product.product', string="Departamento")
    picking_id = fields.Many2one('stock.picking', string='Entrega')
    project_id = fields.Many2one('project.project', string='Poyecto')

    _sql_constraints = [
       ('product_id_unique',
        'UNIQUE(product_id)',
        ("El departamento que eligió, ya está asignado. Por favor, elija otro.")
        ),
    ]

    @api.depends('product_id')
    def get_name(self):
        for record in self:
            self.name = self.product_id.name + " - " + self.project_id.name            

class InmueblesWizard(models.TransientModel): 
    _name = 'inmuebles.wizard'
    _description = 'Asociar cliente con inmueble'
	
    @api.multi
    def asignacion_inmueble(self):    
        context = self._context
        entregas_ids = self.env['stock.picking'].browse(context.get('active_ids'))        
        for actual_entrega in entregas_ids:
            repeated = 'False'
            if actual_entrega.product_id.es_inmueble:
                if actual_entrega.product_id.categ_id.name == 'DEPARTAMENTOS':                    
                    for refer_entrega in entregas_ids:                        
                        if (actual_entrega.product_id.id == refer_entrega.product_id.id) and (actual_entrega.id != refer_entrega.id):                            
                            repeated = 'True'                            
                    
                    # if repeated == 'False' and actual_entrega.id_proyecto and actual_entrega.state == 'done':                        
                    #     inmueble = self.env['inmuebles.helpdesk']
                    #     data = {                        
                    #         'partner_id':actual_entrega.partner_id.id,
                    #         'product_id':actual_entrega.product_id.id,
                    #         'picking_id':actual_entrega.id,
                    #         'project_id':actual_entrega.id_proyecto.id,
                    #     }
                    #     inmueble.create(data)