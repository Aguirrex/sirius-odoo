{
    'name': 'Quindicolor Ventas',
    'version': '1.0',
    'depends': ['sale'],
    'author': 'Quindicolor',
    'category': 'Sales',
    'description': 'Personalización de ventas para Quindicolor',
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': True,
    'license': 'LGPL-3',
}
