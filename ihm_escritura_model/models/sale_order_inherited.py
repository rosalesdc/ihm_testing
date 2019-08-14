#-*- coding: utf-8 -*-

from odoo import api
from odoo import fields
from odoo import models

class SaleOrderInherited(models.Model):
    _inherit = 'sale.order'

    escritura=fields.Char(string="Escritura")

    x_fecha_escritura = fields.Datetime(string = 'Fecha escrituración')

#    @api.model
#    def _get_escritura_date(self):
#        print("ESCRITURA")
        #escritura_asociada=self.env['inmueble.escritura'].search([('orden_venta_id', '=', self.id)], limit=1)

        #if escritura:
        #    for record in escritura:
        #        self.x_fecha_escritura= record.fecha
