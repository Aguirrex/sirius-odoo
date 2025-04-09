from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = 'quindicolor.sale.order'
    _description = 'Sale Order'

    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, default='New')
    date = fields.Date(string='Date', default=fields.Date.today)
    customer_id = fields.Many2one('res.partner', string='Customer', required=True)
    business_line = fields.Char(string='Business Line')
    product_line_ids = fields.One2many('quindicolor.sale.order.line', 'order_id', string='Products')
    notes = fields.Text(string='Notes')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('cancel', 'Cancelled'),
    ], string='State', default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('sale.order.sequence') or 'New'
        return super(SaleOrder, self).create(vals)

    def action_confirm(self):
        self.state = 'confirm'

    def action_cancel(self):
        self.state = 'cancel'

    @api.depends('product_line_ids.subtotal')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.subtotal for line in order.product_line_ids)