# -*- coding: utf-8 -*-

from odoo import models, fields,api,_
from odoo.exceptions import UserError, ValidationError

class Project(models.Model):
    _inherit = "project.project"
    
    rep_contrato_categoria_id = fields.Many2one('product.category',string='Contrato (categoría)', domain = [('x_contrato', '=', True)])
    
    rep_total_categoria = fields.Float (string = 'Total Contratado', compute='_calcula_total_categoria')

    rep_amortizaciones_ids = fields.One2many ('amortizacion.reporte', 'project_id', string = 'Retenciones (amoritzación)', compute='_calcula_retenciones')
    
    rep_total_retenciones = fields.Float (string = 'Total de retenciones')

    rep_pago_ids = fields.Many2many ('account.payment', string = 'Pagos', compute='_calcula_pagos')

    rep_total_pagos = fields.Float (string = 'Total de pagos')

    @api.onchange('rep_contrato_categoria_id')   
    def _calcula_total_categoria(self):
        total=0
        categorias=self.env['qty.budget'].search([('category_id','=',self.rep_contrato_categoria_id.id)])
        for line in categorias:
            #total+=line.qty
            total+=line.cantidad_total
        self.rep_total_categoria=total
    
    @api.onchange('rep_contrato_categoria_id')   
    def _calcula_retenciones(self):
        amortizaciones=self.env['amortizacion.reporte'].search([('categoria_id','=',self.rep_contrato_categoria_id.id)])
        registros_amortizacion=[]
        total_descontado=0
        for amortizacion in amortizaciones:
            registros_amortizacion.append(amortizacion.id or False)
            total_descontado+=amortizacion.cantidad_descontada
            print("Agregando retencion")
        self.rep_amortizaciones_ids = registros_amortizacion
        self.rep_total_retenciones = total_descontado
        #self.rep_amortizaciones_ids : (6, 0,registros_amortizacion )
        #self.write({"rep_amortizaciones_ids": [(6, 0, [registros_amortizacion])]})

    #@api.depends('name')
    @api.onchange('rep_contrato_categoria_id')   
    def _calcula_pagos(self):
        pagos=self.env['account.payment'].search([('x_categoria_id','=',self.rep_contrato_categoria_id.id)])
        registros_pago=[]
        total_pago=0
        for pago in pagos:
            registros_pago.append(pago.id or False)
            total_pago+=pago.amount
        self.rep_pago_ids = registros_pago
        self.rep_total_pagos = total_pago