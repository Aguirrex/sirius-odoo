{
    'name': 'Sirius - Estilos Backend',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Personalización visual del backend para Sirius',
    'depends': ['web'],
    'data': [
        'views/navbar_custom.xml',  
    ],
    'assets': {
        'web.assets_backend': [
            'sirius_theme/static/src/css/backend_styles.css',
            # 'views/assets_backend.xml',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
