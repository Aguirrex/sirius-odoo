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

    x_brand = fields.Many2one('product.brand', string='Marca', help="Marca del producto (ej. Quindicolor, Pintuland, Sika).")

    x_is_paint = fields.Boolean(string="Es Pintura", default=False, 
                              help="Marcar si el producto es pintura para mostrar detalles técnicos específicos.")