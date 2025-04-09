{
    'name': 'Set Default Language',
    'version': '1.0',
    'category': 'Tools',
    'summary': 'Set Spanish as default language automatically',
    'depends': ['base'],
    'data': [
        'data/lang_config.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'post_init_hook': 'set_default_lang_to_all_users',
}
