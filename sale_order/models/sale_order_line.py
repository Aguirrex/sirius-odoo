from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _name = 'quindicolor.sale.order.line'
    _description = 'Sale Order Line'

    product_id = fields.Many2one('product.product', string='Product', required=True)
    description = fields.Text(string='Description')
    quantity = fields.Integer(string='Quantity', default=1)
    price_unit = fields.Float(string='Unit Price')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    order_id = fields.Many2one('quindicolor.sale.order', string='Sale Order')
    
    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit