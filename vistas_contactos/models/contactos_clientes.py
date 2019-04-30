# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class LineasCuentaAnalitica(models.Model):
    _inherit = 'res.partner'
    
    def _get_partner_domain(self):
        #esta funcion devolvera una cadena de tecto de tipo “[1,34,23,45]” con los ids dela tabla res.partner que queremos mostrar.
        res = {}
        for orden in self.browse():
            partners = []
            #Realizamos las consultas necesarias para obtener los Ids que buscamos y los pasamos a la lista “partners”
            #depues debemos pasar la lista a una cadena de texto, existen varias formas.. esta es una de ellas:
            string = ''
            for i in partners:
                string = string + str(i) + ','
            res[orden.id] = '[' + string + ']'
        return res


#    _columns = {
#        'partner_domain': fields.function(_get_partner_domain, method=True, type='char', string='Domain'),
#        'partner_id': fields.many2one('res.partner', 'Partner', required=False, domain="[('id','in',eval(partner_domain) )]"),