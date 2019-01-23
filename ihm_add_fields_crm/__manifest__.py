# -*- coding: utf-8 -*-
{
    'name': "ihm CRM Agregar Campos",

    'summary': """
        Agrega campos para el CRM
    """,

    'description': """
        Agrega campos para el CRM
    """,

    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'crm', # es el nombre de la aplicacion de la que extendemos
        'sale',
        'sale_management',
    ],

    # always loaded
    'data': [
    'views/campos_crm.xml',
    'views/sale_order_inherited.xml',
    'security/ir.model.access.csv',
    ],
    'installable':True,
}

#https://www.odoo.com/es_ES/forum/ayuda-1/question/conditionally-display-or-hide-a-field-in-a-view-13042