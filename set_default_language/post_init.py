from odoo import api, SUPERUSER_ID

def set_default_lang_to_all_users(env):
    users = env['res.users'].search([])
    for user in users:
        user.lang = 'es_CO'