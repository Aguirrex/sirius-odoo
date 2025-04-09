from odoo import api, SUPERUSER_ID

def set_default_lang_to_all_users(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    # Cambiar el idioma de todos los usuarios a 'es_CO'
    users = env['res.users'].search([])
    for user in users:
        user.lang = 'es_CO'
