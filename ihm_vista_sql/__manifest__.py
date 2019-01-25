# -*- coding: utf-8 -*-
{
    'name': "Ejecutar consulta y mostrar en árbol",

    'summary': """
        Ejecutar consulta en Tree""",

    'description': """
        Ejecutar consulta para visualizar en vista de árbol
    """,

    'author': "drc",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','website','contacts','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/my_report_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}

#Notes: 
#Se instaló un paquete tools porque no se reconocía el nombre "pip3 install setuptools-odoo"
#https://odoo-development.readthedocs.io/en/latest/dev/py/postgres-views.html
#https://supportuae.wordpress.com/2017/09/10/creating-tree-view-report-using-sql-query/
#https://sajjadhossain.com/2013/06/30/openerp-7-creating-report-using-sql-query
#https://pypi.org/project/setuptools-odoo/
#https://stackoverflow.com/questions/44797225/get-data-from-different-model-odoo-9