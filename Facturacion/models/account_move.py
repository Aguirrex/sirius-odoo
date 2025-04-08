from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    fact = fields.Char(string='factura', required=True)

    @api.model
    def create(self, vals):
        # Aquí puedes agregar lógica personalizada al crear una factura
        res = super(AccountMove, self).create(vals)
        return res