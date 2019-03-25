# -*- coding: utf-8 -*-
from odoo import http

# class MrpTag(http.Controller):
#     @http.route('/mrp_tag/mrp_tag/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mrp_tag/mrp_tag/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mrp_tag.listing', {
#             'root': '/mrp_tag/mrp_tag',
#             'objects': http.request.env['mrp_tag.mrp_tag'].search([]),
#         })

#     @http.route('/mrp_tag/mrp_tag/objects/<model("mrp_tag.mrp_tag"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mrp_tag.object', {
#             'object': obj
#         })