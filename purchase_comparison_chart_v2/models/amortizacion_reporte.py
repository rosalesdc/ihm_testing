# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models


class AmortizacionReporte(models.Model):
    _name = 'amortizacion.reporte'
    _description = 'Amotización Reporte'

    name = fields.Char(
        string='Registro Amortización'
    )

    purchase_order_id = fields.Many2one(
        'purchase.order',
        string="Purchase Order"
    )

    account_invoice_id = fields.Many2one(
        'account.invoice',
        string='Factura'
    )
    cantidad_descontada = fields.Float(
        string='Cantidad descontada'
    )
    categoria_id = fields.Many2one(
        'product.category',
        string="Contrato (categoría)",
    )

    project_id = fields.Many2one(
        'project.project',
        string = 'Proyecto'
    )

    #fecha_registro = fields.Date(string = 'Fecha')