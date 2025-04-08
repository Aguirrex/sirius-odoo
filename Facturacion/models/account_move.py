from odoo import fields, models, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    fact = fields.Char(string='Campo Extra')


