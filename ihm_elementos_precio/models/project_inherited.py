# -*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class ProyectoElementos(models.Model):
    _inherit = 'project.project'
    x_elementos_ids = fields.One2many(
                                'elementos.precio', #modelo al que se hace referencia
                                'proyecto_id', #un campo de regreso
		string="Elementos de Precio"
		)

    @api.one
    def actualizar_todos_productos(self):
        productos = self.env['product.template'].search([('x_proyecto_id', '=', self.id),('estatus','=','Disponible')])
        for producto in productos:
            importe_total_elementos = sum(line.importe for line in producto.x_asignacion_ids)
            producto.list_price=importe_total_elementos
            print("nuevo precio modificado")
            
            
#        precio_calculado = float(self.importe_total_elementos)
#        self.write({'list_price': precio_calculado})