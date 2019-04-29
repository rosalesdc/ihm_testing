# -*- coding: utf-8 -*-
{
    'name': "ihm_ocultar_campos_inmueble",

    'summary': """
        Ocultar campos de inmuebles""",

    'description': """
        Ocultar campos de inmuebles para usuarios que no son el director
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/ocultar_campos_inmueble.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}