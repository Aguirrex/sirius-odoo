# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'

    happy_user = fields.Boolean(
        string='Happy User',
        default=True)