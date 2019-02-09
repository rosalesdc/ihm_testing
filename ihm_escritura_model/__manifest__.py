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
        'mail',
        'sale',
        'sale_management',
        'crm',
        'ihm_add_fields_crm',
        'ihm_add_fields_productos',
    ],

    # always loaded
    'data': [
    'views/inmueble_escritura_view.xml',
    #'views/venta_escritura_view.xml',
    'views/venta_inherited.xml',
    'security/ir.model.access.csv',
    ],
    'installable':True,
    'auto_install':False,
}

#CAMPO PARA ARCHIVOS ADJUNTOS
#https://www.odoo.com/es_ES/forum/ayuda-1/question/in-binary-field-odoo-v-11-134833
#BUSCAR ELEMENTOS
#https://www.odoo.com/es_ES/forum/ayuda-1/question/how-to-do-a-sql-query-in-odoo-10-119605
#AGREGAR Chatter
#http://www.odooninja.com/add-chatter-existing-model/