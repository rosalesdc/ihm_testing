# -*- coding: utf-8 -*-
{
    'name': "Agrega campos para Productos IHM",

    'summary': """ Campos adicionales para productos IHM
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
        'crm',
        'product',
        'sale',
    ],

    # always loaded
	'data': [
	'views/add_fields_product_view.xml',
        'views/campo_crm_producto.xml',
    ],
	'demo':[

	],
    'installable':True,
}
