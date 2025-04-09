{
    'name': 'QuindiColors Inventario ',
    'version': '1.0',
    'summary': """
        Este módulo gestiona el inventario de QuindiColors
    """,
    'category': 'Inventory',  # Categoría apropiada
    'depends': ['stock'],  # Dependencia del módulo stock
    'data': [
        "security/ir.model.access.csv",
        'data/product_category_data.xml',
        'data/product_data.xml',
        'views/stock_picking_view_inherit.xml',
        "views/product_template_views.xml",
        'views/product_brand_views.xml', 
    ],
    "assets": {
        'web.assets_backend': [
            '/inventory/static/img/product_images/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    "license": 'LGPL-3'
}