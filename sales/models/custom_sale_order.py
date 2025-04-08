# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields

class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'
    _name = 'custom.sale.order'
    _description = 'Custom Sale Order'
    
    happy_user = fields.Boolean(
        string='Happy User',
        default=True)