# -*- coding: utf-8 -*-
{
    'name': "ihm views mods",

    'summary': """
        Modificaciones varias a las vistas
        """,

    'description': """
        Modificaciones a las vistas
        -En contabilidad cambia la etiqueta "Facturas a pagar" por Facturas por cobrar
        -Añadir columna cuenta analítica en la vista de árbol de Pedidos de Compra
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'stock', 'purchase', 'ihm_escritura_model', ],

    # always loaded
    'data': [
        
        'views/contabilidad_inherited_view.xml',
        'views/pedidos_compra_inherited_view.xml',
        'views/kanban_productos_view.xml',
        'views/ventas_add_escritura_view.xml',
        'views/oportunidad_inherited_search.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}