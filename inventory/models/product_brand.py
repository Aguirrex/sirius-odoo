from odoo import models, fields

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Marca de Producto'
    name = fields.Char(string='Nombre Marca', required=True)