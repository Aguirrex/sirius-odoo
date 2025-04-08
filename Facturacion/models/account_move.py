from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'
    fact = fields.Char(string='Campo Extra')