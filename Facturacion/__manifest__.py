{
    'name': 'Facturacion Personalizada',
    'version': '1.0',
    'depends': ['account'],  # <<--- clave: depende de 'account'
    'depends': ['account'],
    'data': [
        'security/ir.model.access.csv',
        'views/account.move.view.xml',
    ],

    'installable': True,
    'auto_install': False,
}
