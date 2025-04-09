from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    x_delivery_zone = fields.Selection([
        ('sincelejo', 'Sincelejo'),
        ('medellin', 'Medellín'),
        ('manizales', 'Manizales'),
        ('armenia', 'Armenia'),
        ('ibague', 'Ibagué'),
        ('dosquebradas', 'Dosquebradas'),
        ('cali', 'Cali'),
        ('popayan', 'Popayán'),
        ('pasto', 'Pasto'),
        ('florencia', 'Florencia'),
        ('neiva', 'Neiva'),
    ], string="Sucursal / Distribuidor de Entrega")
    
    user_id = fields.Many2one('res.users', string='Salesperson')

