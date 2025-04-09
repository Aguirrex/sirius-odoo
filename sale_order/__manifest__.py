{
    'name': 'Ventas Quindicolor',
    'version': '1.0',
    'author': 'Tu Nombre o Empresa',
    'category': 'Sales',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'models/sale_order_line.py',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}