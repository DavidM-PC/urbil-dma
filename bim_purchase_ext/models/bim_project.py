from odoo import models, fields, api, _
from datetime import datetime, date
import logging


class BimProject(models.Model):
    _inherit = 'bim.project'

    purchase_line_ids = fields.Many2many(
        'purchase.order',
        string="Compras")
