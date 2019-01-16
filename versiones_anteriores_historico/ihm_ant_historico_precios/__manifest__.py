# -*- coding: utf-8 -*-
{
    'name': "ihm_historico_precios",

    'summary': """
        Mostrar historico de precios de productos (Purchase Orders)
        """,

    'description': """
        El Usuario selecciona un botón con el cual puede visualizar el histórico de precios del producto,
        el sistema muestra una lista con los siguientes campos:
        Nombre del producto
        Fecha
        Precio
        Proveedor
        Se deben buscar los precios de compra en las órdenes de compra, es decir en las líneas de las órdenes de compra.
        El reporte deberá contener un listado con los precios que un producto ha tenido a través del tiempo,
        dejando un solo renglón por precio hasta que haya uno nuevo, es decir tipo "Select Distinct".
        Si un precio ha permanecido sin cambio, se mostrará la fecha en la que se tuvo ese precio por primera vez.
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase','account','account_accountant'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/purchase_order_line_inherit.xml',
        'views/historico_productos_view.xml',
        'views/button_historico.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}