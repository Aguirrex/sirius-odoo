{
    'name': 'Sirius - Estilos Backend',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Personalización visual del backend para Sirius',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'sirius_theme/static/src/css/backend_styles.css',
            
        ],
    },
    'data': [
        'views/assets_backend.xml',
    ],
    'qweb': [
        'static/src/xml/my_template.xml',
    ],
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}
