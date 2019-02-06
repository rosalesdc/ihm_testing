# -*- coding: utf-8 -*-
{
    'name': "ihm_helpdesk_mods",

    'summary': """
        Agrega modelos a relacionar con el HelpDesk
        """,

    'description': """
        Se realizan modelos asociados a la aplicación de HelpDesk
    """,

    'author': "Soluciones 4G",
    'website': "http://soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
    'base',
    'helpdesk',
    'calendar',
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ticket_form_inherited.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        
    ],
}