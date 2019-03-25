# -*- coding: utf-8 -*-

from odoo import models, fields, api

class mrp_tag(models.Model):
    _inherit = 'mrp.production'

    datetime = fields.Datetime('Fecha y hora')
    manager = fields.Many2one(
        'res.partner',
        'Nombre del encargado.',
        domain=[('category_id.name','ilike','operador')]
    )
    turn = fields.Selection(
        [
            ('Morning','Matutino'),
            ('Vespertino','Vespertino'),
            ('Nocturno','Nocturno')
        ],
        'Turno.'
    )
    product_name = fields.Char(
        'Nombre del producto.',
        related='product_id.name'
    )
    m2 = fields.Float('Metros cuadrados. (m2)', size=2)
    large = fields.Float('Largo del rollo (mts).', size=2)
    wigth = fields.Float('Ancho del rollo (mts).', size=2)
    gr_m2 = fields.Float('Gramaje (gr/m2).', size=2)
    thicknesstest = fields.Integer('Prueba de espesor (mm).', size=2)
    lot_id = fields.Many2one('stock.production.lot', 'No de lote.')
    loation_id = fields.Many2one(
        'stock.location',
        related='location_dest_id'
    )
    confirm_code = fields.Char(
        'Código de rollos que conforman tarima.'
    )


    @staticmethod
    def get_linked_move_lines(self):
        linked_move_lines = self.env['stock.traceability.report']\
                                ._get_linked_move_lines(self)
        if not linked_move_lines:
            return ''
        return ", ".join(linked_move_lines[0].mapped('lot_id.name'))


    @api.multi
    def write(self, values):
        if values.get('state') == 'done':
            self.datetime = fields.datetime.now()
        return super(mrp_tag, self).write(values)
