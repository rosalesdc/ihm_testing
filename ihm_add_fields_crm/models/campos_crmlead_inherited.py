# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import fields
from odoo import models

class CamposResPartner(models.Model):
    _inherit = 'crm.lead'

    def _calcula_numero_dias(self):
        #print("FUNCION!!")
        a = self.create_date
        #print("fecha A: " + str(a))
        b = datetime.now()
        #print("fecha B: " + str(b))
        delta = b - a
        #print("DELTA DAYS!!!")
        #print(delta.days)
        self.dias_desde_creacion=delta.days
        #return delta.days
    
    id_numero_referencia = fields.Many2one(
                                           'numero.referencia',
                                           string="Número de Referencia"
                                           )
                                         
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

    
    dias_desde_creacion = fields.Integer(compute='_calcula_numero_dias')
    

    
    asesor_ventas = fields.Many2one(
                                    'res.partner',
                                    string="Asesor de ventas"
                                    )
    primera_fecha_prospecto=fields.Date(string="Primera fecha de prospecto")

class EntidadFinanciraCbancario(models.Model):
    _name = 'efinanciera.credbancario'
    name = fields.Char(
                       string="Entidad Financiera Credito Bancario",
                       required=True,
                       )
                               
class EntidadFinanciraCofinavit(models.Model):
    _name = 'efinanciera.cofinavit'
    name = fields.Char(
                       string="Entidad Financiera COFINAVIT",
                       required=True,
                       )

class NumeroReferencia(models.Model):
    _name = 'numero.referencia'
    name = fields.Char(
                       string="Número de referencia",
                       required=True,
                       )
                       

                       