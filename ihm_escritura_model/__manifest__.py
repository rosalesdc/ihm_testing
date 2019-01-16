# -*- coding: utf-8 -*-
{
    'name': "IHM Modelo Escrituras",

    'summary': """
        Agrega un modelo Escrituras asociadas a las ventas
    """,

    'description': """
        Agrega un modelo Escrituras asociadas a las ventas
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
        'sale',
        'sale_management',
    ],

    # always loaded
    'data': [
    'views/venta_inherited.xml',
    'security/ir.model.access.csv',
    ],
    'installable':True,
}
