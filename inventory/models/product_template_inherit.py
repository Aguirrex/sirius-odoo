# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    x_base_type = fields.Selection([
        ('agua', 'Agua'),
        ('aceite', 'Aceite'),
        ('epoxica', 'Epóxica'),
        ('poliuretano', 'Poliuretano'),
        ('nitro', 'Nitro')
        # Puedes agregar más opciones aquí
    ], string='Tipo Base', help="Tipo de base del producto para filtrado y reportes.")

    x_finish = fields.Selection([
        ('mate', 'Mate'),
        ('satinado', 'Satinado'),
        ('brillante', 'Brillante')
        # Puedes agregar más opciones aquí
    ], string='Acabado', help="Acabado final del producto.")

    x_use = fields.Selection([
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
        ('metal', 'Metal'),
        ('madera', 'Madera'),
        ('pared', 'Pared')
        # Puedes agregar más opciones aquí
    ], string='Uso Recomendado', help="Uso principal recomendado para el producto.")

    x_performance = fields.Float(string='Rendimiento (m²/galón)', help="Rendimiento aproximado del producto por galón.")

    # Asegúrate de que el modelo 'product.brand' exista o créalo.
    # Si prefieres algo más simple, puedes cambiarlo a fields.Char o fields.Selection.
    x_brand = fields.Many2one('product.brand', string='Marca', help="Marca del producto (ej. Quindicolor, Pintuland, Sika).")

# Nota: Si el modelo 'product.brand' no existe, necesitarás crearlo en otro archivo, por ejemplo:
# models/product_brand.py
# from odoo import models, fields
# class ProductBrand(models.Model):
#     _name = 'product.brand'
#     _description = 'Marca de Producto'
#     name = fields.Char(string='Nombre Marca', required=True)
#     # Otros campos relevantes...

# No olvides agregar los nuevos archivos Python al __init__.py de tu carpeta 'models'
# y actualizar las vistas XML para mostrar estos campos en la interfaz de usuario del producto.
# También actualiza los permisos de acceso si es necesario.