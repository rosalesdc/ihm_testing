# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class SaleOrderMod(models.Model):
    _inherit = 'sale.order'

    @api.multi
    def _obtener_elementos(self):
        elementos=""
        print (elementos)
#        for lines in self.order_line:
#            elementos+=lines.product_id.name+", "
#        self.rep_productos=elementos
        
    #@api.one
    @api.model
    def create(self, vals):
        #self.ensure_one()
        res = super(SaleOrderMod, self).create(vals)
        for record in res:
            print(record.id_asesor_ventas.name)
            record.nombre_asesor=record.id_asesor_ventas.name
            print(record.nombre_asesor)
        return res
        
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
    
    tipo_credito = fields.Selection(
                                    selection=[
                                    ('COFINAVIT', 'COFINAVIT'),
                                    ('Crédito Bancario', 'Crédito Bancario'),
                                    ('Infonavit/Fovisste', 'Infonavit/Fovisste'),
                                    ('Efectivo', 'Efectivo'),
                                    ],
                                    string="Tipo de credito"
                                    )
    
    cantidad_pagar_cbancario = fields.Float(
                                            string="Cantidad a pagar credito bancario",
                                            default=0.0,
                                            required=True, )
    
    cantidad_pagar_infonavitfov = fields.Float('Cantidad a pagar INFONAVIT/FOVISTE', (10, 2))
    
    cantidad_pagar_efectivo = fields.Float('Cantidad a pagar Efectivo', (10, 2))
    
    id_entidad_financiera = fields.Many2one(
                                            'res.bank',
                                            string="Entidad Financiera"
                                            )
    id_asesor_ventas = fields.Many2one(
                                    'res.partner',
                                    string="Asesor de ventas"
                                    )
    
    nombre_asesor=fields.Char(string="Asesor")                                
    productos_reporte=fields.Char(string="Otros Inmuebles", default="-", compute='_obtener_elementos', store=True) 
    
                                    
class OrderLinesProduct(models.Model):
    _inherit = 'sale.order.line'

    #Añade la orden de Venta al Inmueble, para reporte
    @api.multi
    def create(self, vals):
        res_id = super(OrderLinesProduct, self).create(vals)
        for record in res_id:
            if record.product_id.es_inmueble==True:
                record.product_id.sale_order=record.order_id
        return res_id

   