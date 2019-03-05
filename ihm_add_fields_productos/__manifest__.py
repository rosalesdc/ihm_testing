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
        'project',
        'ihm_add_fields_proyecto',#para obtener el equipo de entrega del proyecto

    ],

    # always loaded
	'data': [
        'security/ir.model.access.csv',
	'views/add_fields_product_view.xml',
        'views/campo_crm_producto.xml',
        #'views/reporte_inmueble.xml',
    ],
	'demo':[

	],
    'installable':True,
}

#envio de correos
#https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-send-email-in-openerp-by-python-code-72118
#https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-send-email-from-html-form-112029