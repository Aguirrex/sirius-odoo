from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = 'quindicolor.sale.order'
    _description = 'Orden de Venta Quindicolor'

    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default='Nuevo')
    date = fields.Date(string='Fecha', default=fields.Date.today, required=True)
    customer_id = fields.Many2one('res.partner', string='Cliente', required=True)
    business_line = fields.Selection([
        ('madera', 'Madera'),
        ('ferreteria', 'Ferretería'),
        ('arquitectura', 'Arquitectura'),
        ('adhesivos', 'Adhesivos'),
        ('automotriz', 'Automotriz'),
    ], string='Línea de Negocio', required=True)
    product_line_ids = fields.One2many('quindicolor.sale.order.line', 'sale_order_id', string='Productos')
    total_amount = fields.Float(string='Monto Total', compute='_compute_total', store=True)
    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirm', 'Confirmado'),
        ('cancel', 'Cancelado')
    ], default='draft', string='Estado')
    notes = fields.Text(string='Notas')

    @api.depends('product_line_ids.subtotal')
    def _compute_total(self):
        for record in self:
            record.total_amount = sum(record.product_line_ids.mapped('subtotal'))

    def action_confirm(self):
        self.state = 'confirm'

    def action_cancel(self):
        self.state = 'cancel'

class SaleOrderLine(models.Model):
    _name = 'quindicolor.sale.order.line'
    _description = 'Línea Orden de Venta Quindicolor'

    sale_order_id = fields.Many2one('quindicolor.sale.order', string='Orden de Venta')
    product_id = fields.Many2one('product.product', string='Producto', required=True)
    description = fields.Char(string='Descripción')
    quantity = fields.Integer(string='Cantidad', default=1)
    price_unit = fields.Float(string='Precio Unitario')
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
