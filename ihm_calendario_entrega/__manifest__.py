# -*- coding: utf-8 -*-
{
    'name': "ihm_calendario_entrega",

    'summary': """
        Agendar citas para entrega de inmuebles
        """,

    'description': """
        Agendar citas para entregas de inmuebles
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
    'stock',
    'sale',
    'sale_management'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'views/calendario_entrega_view.xml',
        'views/smart_button_citas.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}