# -*- coding: utf-8 -*-
{
    'name': "ihm print saleorder",

    'summary': """
        Modificaciones a las ordenes y pedidos de ventas
        """,

    'description': """
        Modificaciones a las ordenes y pedidos de ventas
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_management','sale'],

    # always loaded
    'data': [
        'views/saleorder_print_inherited_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}