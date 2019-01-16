# -*- coding: utf-8 -*-
{
    'name': "Modulo de historico",

    'summary': """
    """,

    'description': """
        
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
        'stock',
        'purchase',
        'account',
        'account_accountant',
    ],

    # always loaded
    'data': [
        'views/purchase_order_line_inherit.xml',
        'views/historico_view.xml',
        'views/button_smart.xml',
    ],
    'installable':True,
    'auto_install':False,
}