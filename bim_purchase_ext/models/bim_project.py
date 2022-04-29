from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class BimProject(models.Model):
    _inherit = 'bim.project'

    purchase_line_ids = fields.Many2many(
        'purchase.order',
        string="Compras",
        compute="compute_purchases")


    def compute_purchases(self):
    # Función para relacionar compras a obras
        for record in self:
            purchases = self.env['purchase.order'].search([('project_id','=',self.id)])
            if purchases:
                record.purchase_line_ids = purchases.ids
            else:
                record.purchase_line_ids = False
