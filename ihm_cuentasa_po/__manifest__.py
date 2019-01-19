# -*- coding: utf-8 -*-
{
    'name': "ihm_cuentasa_po",

    'summary': """
        Agrega la cuenta analitica en las lineas de PO
        """,

    'description': """
        Agrega la cuenta analítica seleccionada en la PO
        a cada una de las líneas
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
                'purchase',
                'account',
                'analytic',
                'po_cuenta_analitica',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'views/po_ca_inherited_view.xml',
    ],
    'installable' : True,
    # only loaded in demonstration mode
    'demo': [
    ],
}