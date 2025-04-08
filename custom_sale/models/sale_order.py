# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class CustomSaleOrder(models.Model):
    _name = 'sale.order.custom'
    _inherit = 'sale.order'

    x_custom_field = fields.Char(
        string='Happy User')