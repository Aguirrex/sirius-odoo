{
    'name': 'Venta Personalizada Quindicolor',
    'version': '1.0',
    'depends': ['sale'],
    'author': 'Quindicolor',
    'category': 'Sales',
    'description': 'Personalización de ventas para Quindicolor',
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/portal_quote_hide.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
