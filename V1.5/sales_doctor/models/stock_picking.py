# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date
from dateutil.relativedelta import relativedelta


class StockInherit(models.Model):
    _inherit = 'stock.picking'

    doctor_sale_order = fields.Many2one(
        'res.partner',
        string='Doctor',
        related='sale_id.doctor_sale_id',
        store=True,
        readonly=True
    )

    payment_term_id = fields.Many2one(
        'account.payment.term',
        string='Payment Term',
        related='sale_id.payment_term_id',
        store=True,
        readonly=True
    )
    nurse = fields.Char(string="Nurse")
    nurse_assistant = fields.Char(string="Nursing assistant")
    e_device = fields.Integer(string="E-device")
