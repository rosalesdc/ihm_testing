# -*- coding: utf-8 -*-

from odoo import fields
from odoo import models

class ContactosClientes(models.Model):
    _inherit = 'res.partner'
    # def _get_partner_domain(self):
    #     res = {}
    #     contactos=self.env['res.partner'].search([('customer', '=', 'True')])
    #     for contacto in contactos:
    #
    #
    #     for orden in self.browse():
    #         partners = []
    #         string = ''
    #         for i in partners:
    #             string = string + str(i) + ','
    #         res[orden.id] = '[' + string + ']'
    #     return res

    name=fields.Char(groups='ihm_ocultar_validar.group_no_editarcrear')
    partner_domain = fields.Char(string="dominio", default="[557,1413]")
    
    partner_id = fields.Many2one(
                                 'res.partner',
                                 domain="[('id','=',8 )]")
    
#    _columns = {
#        'partner_domain': fields.function(_get_partner_domain, method=True, type='char', string='Domain'),
#        'partner_id': fields.many2one('res.partner', 'Partner', required=False, domain="[('id','in',eval(partner_domain) )]"),
