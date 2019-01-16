# -*- coding: utf-8 -*-
from odoo import http

# class IhmHistoricoPrecios(http.Controller):
#     @http.route('/ihm_historico_precios/ihm_historico_precios/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ihm_historico_precios/ihm_historico_precios/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ihm_historico_precios.listing', {
#             'root': '/ihm_historico_precios/ihm_historico_precios',
#             'objects': http.request.env['ihm_historico_precios.ihm_historico_precios'].search([]),
#         })

#     @http.route('/ihm_historico_precios/ihm_historico_precios/objects/<model("ihm_historico_precios.ihm_historico_precios"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ihm_historico_precios.object', {
#             'object': obj
#         })