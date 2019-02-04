# -*- coding: utf-8 -*-
{
    'name': "ihm_add_fields_proyecto",

    'summary': """
        Agrega campos para la Aplicacion de Proyecto""",

    'description': """
        Agrega campos para la Aplicacion de Proyecto
        -Cantidad para Apartado
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'project',
                ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_view_form_inherited.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}