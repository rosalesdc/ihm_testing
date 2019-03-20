{
    'name': "Agregar Reporte de Entregas",

    'summary': """
    Agrega un reporte de entregas en Inventario->Informes->Entregas
    """,

    'description': """
        Módulo para agregar un menú que permite generar las opciones de las Especificaciones de las piedras
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
        'stock',
        'sale',
        'sale_management',
        'ihm_estatus_entregas',
        
    ],

    # always loaded
    'data': [
        'views/add_reporte_entregas.xml',
    ],
    'installable':True,
    'auto_install':False,
}