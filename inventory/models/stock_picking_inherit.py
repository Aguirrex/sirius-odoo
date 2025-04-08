# -*- coding: utf-8 -*-
from odoo import models, fields, api, _ # Importaciones necesarias
from odoo.exceptions import UserError    # Para lanzar errores si es necesario

class StockPickingInherit(models.Model):
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

    # --- 2. Modificar atributos de un campo existente ---
    note = fields.Text(
        string="Notas Internas Personalizadas",
    )

    # --- 3. Sobrescribir un método existente ---
    def button_validate(self):
        for picking in self:
            if picking.x_requiere_revision_calidad and not picking.x_referencia_externa:
                raise UserError(_("La transferencia requiere revisión de calidad, por favor, añada la 'Referencia Externa' antes de validar."))
 
        res = super(StockPickingInherit, self).button_validate()

        return res

    # --- 4. Añadir un nuevo método ---
    def mi_accion_personalizada(self):

        self.ensure_one()

        if not self.x_referencia_externa:
             self.x_referencia_externa = 'ACCION_EJECUTADA'

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _('Acción Ejecutada'),
                'message': _('Mi acción personalizada se ejecutó en %s.') % self.name,
                'sticky': False,
            }
        }