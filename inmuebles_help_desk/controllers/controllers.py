# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm

class WebsiteForm(WebsiteForm):
    @http.route('''/helpdesk/<model("helpdesk.team", "[('use_website_helpdesk_form','=',True)]"):team>/submit''', type='http', auth="public", website=True)
    def website_helpdesk_form(self, team, **kwargs):
        if not team.active or not team.website_published:
            return request.render("website_helpdesk.not_published_any_team")
        default_values = {}
        if request.env.user.partner_id != request.env.ref('base.public_partner'):            
            entregas = request.env['inmuebles.helpdesk'].sudo().search([('partner_id','=',request.env.user.partner_id.id)])
            categorias = request.env['categoria.falla'].sudo().search([])
            print('******************* CATEGORIAS *******************')
            print(categorias)
            default_values['name'] = request.env.user.partner_id.name
            default_values['email'] = request.env.user.partner_id.email            
        return request.render("website_helpdesk_form.ticket_submit", {'team': team, 'default_values': default_values, 'entregas':entregas, 'categorias':categorias})