from odoo import api, SUPERUSER_ID

# Cambia la firma de la función para aceptar solo 'env'
def set_default_lang_to_all_users(env):
    # Ya no necesitas crear el 'env' manualmente, se recibe como argumento
    # env = api.Environment(cr, SUPERUSER_ID, {}) # Elimina o comenta esta línea
    users = env['res.users'].search([])
    for user in users:
        # Asegúrate de que el idioma 'es_CO' esté cargado en tu instancia de Odoo
        user.lang = 'es_CO'