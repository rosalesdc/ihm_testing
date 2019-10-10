# -*- encoding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Purchase Comparison Chart',
    'version': '1.2',
    'category': 'Purchase',
    'author':'PPTS [India] Pvt.Ltd.',
    'description': """
    Purchase Comparison Chart
    """,
    'license': 'LGPL-3',
    'summary': 'Purchase Comparison Chart',
    'depends': ['purchase','website', 'purchase_requisition','budget_management_v2'],
    'website': 'https://www.pptssolutions.com',
    'data': [
        'views/inherit_purchase_requisition_view.xml',
        'views/purchase_order.xml',
        'views/bid_templates.xml',
        'views/amortizacion_reporte_views.xml',
        'views/account_payment_analitica.xml',
        'views/product_list_view_inherit.xml',
        'views/reporte_pagos_retenciones.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 105,
}
