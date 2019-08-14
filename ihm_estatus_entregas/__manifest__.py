# -*- coding: utf-8 -*-
{
    'name': "IHM estados entrega",
    'description': """
        Generar nuevo estado en transferencias
    """,
    'author': "Soluciones4G",
    'website': "http://www.soluciones4g.com",
    'version': '0.1',
    'depends': ['base',
    'stock',
    'ihm_add_fields_productos',
    'ihm_escritura_model',
    ],
    'data': [
        'views/stock_picking_state.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/estatus_entregas.xml',
        ],
    'installable':True,
    'auto_install':False,
}
