# -*- coding: utf-8 -*-
{
    'name': "Contactos clientes",

    'summary': """
        solo muesta contactos de tipo cliente a usuarios de ventas""",

    'description': """
        solo muesta contactos de tipo cliente a usuarios de ventas
    """,

    'author': "soluciones 4G",
    'website': "soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
    'base'
    ,'contacts'
    ,],

    # always loaded
    'data': [
        'views/views_contactos_cliente.xml',
        #'views/ocultar_qtybutton_view.xml', esta operación mejor se hace directo en la vista
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
