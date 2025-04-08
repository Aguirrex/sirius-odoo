{
    'name': 'QuindiColors Inventario ',
    'version': '1.0',
    'summary': """
        Este módulo gestiona el inventario de QuindiColors
    """,
    'category': 'Inventory',  # Categoría apropiada
    'depends': ['stock'],  # Dependencia del módulo stock
    'data': [
        'views/stock_picking_view_inherit.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    "license": 'LGPL-3'
}