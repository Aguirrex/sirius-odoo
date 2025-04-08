{
    'name': 'Facturación personalizada',
    'version': '1.0',
    'depends': ['account'],  # por ejemplo si vas a heredar de account.invoice
    'data': [
        'security/ir.model.access.csv',
        'views/invoicing.xml',
    ],
    'installable': True,
    'auto_install': False,
}
