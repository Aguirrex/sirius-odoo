from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_delivery_zone = fields.Selection([
        ('zona_norte', 'Zona Norte'),
        ('zona_sur', 'Zona Sur'),
        ('zona_centro', 'Zona Centro'),
    ], string="Zona de Entrega")

