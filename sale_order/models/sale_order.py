from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_delivery_zone = fields.Selection([
    ('armenia_jardines', 'Armenia, Quindío - Calle 51 No. 13-06 Jardines'),
    ('armenia_centro', 'Armenia, Quindío - Calle 21 No. 18-57 Centro'),
    ('dosquebradas_badea', 'Dosquebradas, Risaralda - Calle 9 N° 5T - 120 La Badea'),
    ('cali_centro', 'Cali, Valle del Cauca - Cra. 8 No 18 - 69 Local 101 Centro'),
], string="Sucursal de Entrega")

    user_id = fields.Many2one('res.users', string='Salesperson')

