# -*- coding: utf-8 -*-
from odoo import api
from odoo import fields
from odoo import models

class PurchaseOrderLinesIn(models.Model): 
    _inherit = 'purchase.order.line'

    def _prepareHistorico(self, consulta, consulta2, self2=1):
        print("preparando valores")
        print(type(self))
        print(type(consulta))
        print(type(consulta2))
        for columnas in consulta2:
                print(columnas)
        return{
        'product_id':consulta2[0],
        'price_unit':consulta2[1],
        'date_order':consulta2[4],
        'partner_id':consulta2[3],
        }
        
    @api.model
    def create(self, vals):
        print("CREATING VALUES:::::::::::::::::::::::::")
        ultimo_precio = -1 #un precio que no deba existir
        valores_historico = {}
        
        
        #se obtiene el ultimo precio registrado del producto que se está ingresando, puede diferir del la fecha de su orden
        query = "select product_id,price_unit,order_id,partner_id,create_date from purchase_order_line WHERE product_id= %s ORDER BY create_date DESC LIMIT 1;"
        self.env.cr.execute(query, (vals['product_id'],))
        row = self.env.cr.fetchone()
        
        if row is None:
            print('La consulta regresa NONE--si se agrega al historico')
            res = super(PurchaseOrderLinesIn, self).create(vals)
            #---------Obtener fecha de la orden
            print('fecha pedido')
            id_=int (res['order_id'])
            fecha = self.env['purchase.order'].search([('id', '=', id_)], limit=1)
            date_o=fecha.date_order
            print(date_o)
            #---------
            #Esta tupla sería utilizando la fecha de creación de la línea
            #tupla=(int (res['product_id']),res['price_unit'],res['create_date'],int (res['partner_id']),res['create_date'])
            #Esta tupla sería utilizando la fecha de la orden
            tupla=(int (res['product_id']),res['price_unit'],date_o,int (res['partner_id']),date_o)
            valores_historico=self._prepareHistorico(self,tupla)
            self.env['historico.variaciones'].create(valores_historico)
            return res
        
        else:
            print('La consulta no regresa NONE')
            res = super(PurchaseOrderLinesIn, self).create(vals)
            ultimo_precio = row[1]
            
            #---------Obtener fecha de la orden
            print('fecha pedido')
            id_=int (res['order_id'])
            fecha = self.env['purchase.order'].search([('id', '=', id_)], limit=1)
            date_o=fecha.date_order
            print(date_o)
            #---------
            
            if ultimo_precio == res['price_unit']:
                print("es igual--no se agrega al historico")
            else:
                print("es diferente-- si se agrega al historico")
                #Esta tupla sería utilizando la fecha de creación de la línea
                #tupla=(int (res['product_id']),res['price_unit'],res['create_date'],int (res['partner_id']),res['create_date'])
                #Esta tupla sería utilizando la fecha de la orden
                tupla=(int (res['product_id']),res['price_unit'],date_o,int (res['partner_id']),date_o)
                valores_historico = self._prepareHistorico(self, tupla)
                self.env['historico.variaciones'].create(valores_historico)
            return res
        return res
    

    #https://groups.google.com/forum/#!topic/openerp-spain-users/F6coQY-_AIQ
    #http://linkode.org/crzg1ABc81sHxXegbgSI26
    #https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-do-a-sql-query-in-odoo-10-119605
    #https://www.odoo.yenthevg.com/override-create-functions-odoo/
    
    
        