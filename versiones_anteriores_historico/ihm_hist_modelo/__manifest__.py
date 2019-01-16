# -*- coding: utf-8 -*-
{
    'name': "Modelo para histórico",

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
        'views/historico_variaciones_tree.xml',
        'views/historico_view.xml',
        'views/button_smart.xml',
        'security/ir.model.access.csv',
    ],
    'installable':True,
    'auto_install':False,
}