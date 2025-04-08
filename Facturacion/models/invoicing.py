from odoo import models, fields

class AccountMoveCustom(models.Model):
    _inherit = 'account.move'  # heredas el modelo original

    # Ejemplo de campo personalizado
    tipo_factura = fields.Selection([
        ('a', 'Tipo A'),
        ('b', 'Tipo B'),
    ], string="Tipo de Factura")

class MiFactura(models.Model):
    _name = 'mi.factura'
    name = fields.Char()
