# -*- coding: utf-8 -*-
{
    'name': "ihm CRM Agregar Campos",

    'summary': """
        Agrega campos para el CRM
    """,

    'description': """
        Agrega campos para el CRM
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
        'sale',
        'sale_management',
        'stock',
        'ihm_add_fields_productos',#esta dependencia ya que los productos deben tener los estados
    ],

    # always loaded
    'data': [
    #'views/vista_crm_sale_button.xml', ESTO ERA PARA AGREGAR EN EL CONTEXTO EL NUMERO DE REFERENCIA
    'views/campos_crm.xml',
    'views/payment_sale_orders.xml',
    'views/sale_order_inherited.xml',
    'security/ir.model.access.csv',
    ],
    'installable':True,
}


#https://www.odoo.com/es_ES/forum/ayuda-1/question/conditionally-display-or-hide-a-field-in-a-view-13042

##LLAMAR A UNA VISTA
#https://www.odoo.com/es_ES/forum/ayuda-1/question/create-window-action-button-using-xml-id-112510

#PASAR PARAMETRO A UNA VISTA
#https://stackoverflow.com/questions/34926074/odoo-context-field-default-value-for-popup

#BOTON QUE ABRE UNA VISTA
#https://www.odoo.com/es_ES/forum/ayuda-1/question/create-window-action-button-using-xml-id-112510

#REDEFINIR METODOS
#https://emperove.gitbooks.io/fundamentos-de-desarrollo-odoo-10/content/capitulo-3.html