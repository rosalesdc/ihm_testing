# -*- coding: utf-8 -*-
from odoo import fields
from odoo import models
from odoo import api

class PurchaseOrderLinesIn(models.Model): 
    _inherit='purchase.order.line'
    
    @api.multi
    def _write_values(self, self2=1):
        print("WRITE VALUES:::::::::::::::::::::::::")
        query="select product_id,price_unit,order_id,partner_id,create_date from purchase_order_line WHERE product_id= %s ORDER BY create_date DESC LIMIT 1;"
        for record in self:
            self.env.cr.execute(query, (record.product_id.id,))
            ultimo_precio=self.env.cr.fetchone()[0]
            print(str(ultimo_precio))
        return True

    @api.model
    def create(self, vals):
        print("CREATING VALUES:::::::::::::::::::::::::")
        ultimo_precio=0
        #se obtiene el ultimo precio registrado del producto que se está ingresando
        query="select product_id,price_unit,order_id,partner_id,create_date from purchase_order_line WHERE product_id= %s ORDER BY create_date DESC LIMIT 1;"
        self.env.cr.execute(query, (vals['product_id'],))
        row = self.env.cr.fetchone()
        if row is not None: #si es la primera orden puede regresar None
            ultimo_precio=row[1] 
            #ultimo_precio=self.env.cr.fetchone()[1]
        
        #se almacena el nuevo registro
        res=super(PurchaseOrderLinesIn, self).create(vals)
        #revisa si el ultimo precio es igual al precio que se está registrando
        if ultimo_precio==res['price_unit']:
            res['x_precio_nuevo'] = False
            print("es igual")
        else:
            res['x_precio_nuevo'] = True
            print("es diferente")
        return res
    
    x_precio_nuevo=fields.Boolean(default=True)

    #https://groups.google.com/forum/#!topic/openerp-spain-users/F6coQY-_AIQ
    #http://linkode.org/crzg1ABc81sHxXegbgSI26
    #https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-do-a-sql-query-in-odoo-10-119605
    #https://www.odoo.yenthevg.com/override-create-functions-odoo/
    
    
        