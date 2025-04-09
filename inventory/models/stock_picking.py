# -*- coding: utf-8 -*-
from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    x_referencia_externa = fields.Char(
        string="Referencia Externa",
        copy=False,
        tracking=True,
        help="Número de referencia o código del sistema externo relacionado."
    )
    x_requiere_revision_calidad = fields.Boolean(
        string="Revisión de Calidad Requerida",
        default=False,
        tracking=True
    )