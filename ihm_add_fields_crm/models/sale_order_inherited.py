# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class SaleOrderMod(models.Model):
    _inherit = 'sale.order'

    opportunity_id = fields.Many2one(
                                     'crm.lead',
                                     string='Oportunidad',
                                     )

#    x_id_numero_referencia = fields.Many2one(
#                                             string='Número de Referencia',                                             
#                                             related='opportunity_id.id_numero_referencia',
#                                             )

    id_numero_referencia = fields.Many2one(
                                           'numero.referencia',
                                           string="Número de Referencia",
                                           copy=False
                                           )
                    
    pagos_ids = fields.Many2many(
                                 'account.payment',
                                 string="Pago",
                                 store=True,
                                 )
                                
    id_proyecto = fields.Many2one(
                                  'project.project',
                                  string="Proyecto asociado"
                                  )

    expediente_apartado = fields.Date(string="Fecha de apartado")
    expediente_contrato = fields.Date(string="Fecha de contrato")
    expediente_ingreso_ifinanciera = fields.Date(string="Fecha de ingreso a institución financiera")
    expediente_autorizacion_ifinanciera = fields.Date(string="Autorización de institucion financiera")
    expediente_avaluo = fields.Date(string="Fecha de solicitud de avaluo")
    expediente_instruccion_ifinanciera = fields.Date(string="Fecha de instrucción de institución financiera")
    expediente_firma = fields.Date(string="Fecha de firma")