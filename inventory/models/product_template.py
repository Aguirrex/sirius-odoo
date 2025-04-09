# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
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


    @api.depends('categ_id')
    def _compute_show_technical_details(self):
        madera_category = self.env.ref('inventory.product_category_madera')
        arquitectura_category = self.env.ref('inventory.product_category_arquitectura')
        automotriz_category = self.env.ref('inventory.product_category_automotriz')
        for record in self:
            record.x_show_technical_details = record.categ_id in (madera_category | arquitectura_category | automotriz_category)