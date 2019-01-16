# -*- coding: utf-8 -*-
from odoo import http

class Academy(http.Controller):
#    @http.route('/academy/academy/', auth='public')
#    def index(self, **kw):#index nombre arbitrario de la función
#        return http.request.render('ejercicios01.index', {#nombre del módulo e index es por la página default
#            'alumno':'david','teachers': ["Diana Padilla", "Jody Caroll", "Lester Vaughn"],
#        })
        
    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, ** kw):
        Teachers = http.request.env['ejercicios01.teachers'] #nombre del modelo
        return http.request.render('ejercicios01.indexa', {
                                   'teachers': Teachers.search([])
                                   })
    
#    @http.route('/academy/<name>/', auth='public', website=True)
#    def teacher(self, name):
#        #return '<h1>{}</h1>'.format(name)
#        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    
#    @http.route('/academy/<int:id>/', auth='public', website=True)
#    def teacher(self, id):
#        return '<h1>{} ({})</h1>'.format(id, type(id).__name__)
    
    @http.route('/academy/<model("ejercicios01.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('ejercicios01.biography', {
            'person': teacher
        })