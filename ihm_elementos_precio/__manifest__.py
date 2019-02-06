# -*- coding: utf-8 -*-
{
    'name': "ihm_elementos_precio",

    'summary': """
        Modelo generar elementos de precio - Proyectos
        """,

    'description': """
        Modelo para generar elementos de precio para los proyectos
    """,

    'author': "Soluciones4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'project',
    'stock',
    #'ihm_add_fields_productos', #para acceder a los elementos de precio registrados en productos
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/project_form_view_inherited.xml',
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}