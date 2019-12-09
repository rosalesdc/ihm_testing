# -*- coding: utf-8 -*-
{
    'name': "Asociación Inmuebles",

    'summary': """
        Módulo para asociar cliente e inmueble
    """,

    'description': """
        Módulo para asociar cliente e inmueble
    """,

    'author': "Omar Gómez",
    'website': "http://www.soluciones4g.com",
    
    'category': 'Uncategorized',
    'version': '0.1',
    
    'depends': ['base',
                'stock',
                'contacts',
                'ihm_add_fields_productos',
                'ihm_estatus_entregas',
                'ihm_add_fields_crm',
                'website_helpdesk_form',
                'website_helpdesk',
                'helpdesk',                
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
}