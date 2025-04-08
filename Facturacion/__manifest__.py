{
    'name': 'Facturacion',
    'version': '1.0',
    'summary': 'Personalizaciones para el módulo de facturación',
    'description': """
        Este módulo personaliza el módulo de facturación de Odoo.
        Agrega campos personalizados y modifica vistas.
    """,
    'author': 'Tu Nombre',
    'website': 'http://www.tuweb.com',
    'category': 'Account',
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account.move.view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}