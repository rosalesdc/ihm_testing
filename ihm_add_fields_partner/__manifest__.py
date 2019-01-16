# -*- coding: utf-8 -*-
{
    'name': "ihm Contactos Agregar Campos",

    'summary': """
        Agrega campos para contactos
    """,

    'description': """
        Agrega campos para contactos
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
        'contacts', # es el nombre de la aplicacion de la que extendemos
    ],

    # always loaded
    'data': [
    'views/campos_res_partner.xml',
    'security/ir.model.access.csv',
    ],
    'installable':True,
}
