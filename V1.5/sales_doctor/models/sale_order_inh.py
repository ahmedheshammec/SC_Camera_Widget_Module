# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError

SALE_ORDER_STATE = [
    ('draft', "Reception"),
    ('sent', "Scope Sent"),
    ('sale', "Pre Recovery"),
    ('endoscopy', "Endoscopy"),
    ('post_recovery', "Post Recovery"),
    ('dis_change', "Discharge"),
    ('cancel', "Cancelled"),
]


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    state = fields.Selection(selection=SALE_ORDER_STATE, string="Status", readonly=True, copy=False, index=True,
                             tracking=3, default='draft')
    doctor_sale_id = fields.Many2one('res.partner', string='Doctor', domain=[('is_doctor', '=', True)])

    draft_date = fields.Datetime(string="Reception Date", copy=False, readonly=True,
                                 default=lambda self: fields.Datetime.now())
    per_recovery_date = fields.Datetime(string="per Recovery Date", readonly=True)
    endoscopy_date = fields.Datetime(string="Endoscopy Date", readonly=True)
    post_recovery_date = fields.Datetime(string="Post Recovery Date", readonly=True)
    dis_change_date = fields.Datetime(string="Discharge Date", readonly=True)

    medical_endoscope_id = fields.Many2one('medical.endoscopes', string='Related Endoscope')
    medical_endoscope_count = fields.Integer(string='Endoscope Count', compute='_compute_medical_endoscope_count')

    to_order_duration = fields.Char(string="Per Recovery", compute='_compute_durations')
    to_endoscopy = fields.Char(string="Endoscopy", compute='_compute_durations', )
    to_post_recovery = fields.Char(string="Post Recovery", compute='_compute_durations', )
    to_discharge = fields.Char(string="Discharge", compute='_compute_durations', )

    def _create_invoices(self, grouped=False, final=False, date=None):
        state = self.state
        self.state = 'sale'
        res = super()._create_invoices(grouped, final, date)
        self.state = state
        return res

    def action_create_medical_endoscopes(self):
        self.ensure_one()
        medical_endoscope_rec = self.env['medical.endoscopes'].create({
            'doctor_id': self.doctor_sale_id.id,
            'patient_id': self.partner_id.id,
            'sale_order_id': self.id,
            # Add more fields as needed
        })
        self._compute_medical_endoscope_count()

    @api.depends('medical_endoscope_id')
    def _compute_medical_endoscope_count(self):
        for record in self:
            related_endoscopes = self.env['medical.endoscopes'].search([('sale_order_id', '=', record.id)])
            record.medical_endoscope_count = len(related_endoscopes)

    def action_view_medical_endoscopes(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Related Endoscopes',
            'view_mode': 'form',
            'res_model': 'medical.endoscopes',
            'domain': [('sale_order_id', '=', self.id)],
            'context': "{'create': False}",
        }

    def action_confirm(self):
        """ Confirm the sale orders and set per_recovery_date to now for each."""
        for order in self:
            if not order.per_recovery_date:
                order.per_recovery_date = fields.Datetime.now()
        super(SaleOrder, self).action_confirm()
    # def action_confirm(self):
    #     """Confirm the sale orders and set per_recovery_date to now for each.
    #     Additionally, allow reconfirmation after discharge to enable invoice creation."""
    #     for order in self:
    #         if not order.per_recovery_date:
    #             order.per_recovery_date = fields.Datetime.now()
    #         # Allow moving the order back to 'sale' state from 'dis_change' or any other state.
    #         if order.state in ['dis_change', 'post_recovery', 'endoscopy', 'cancel']:
    #             order.write({'state': 'sale'})
    #     super(SaleOrder, self).action_confirm()

    def action_endoscopy(self):
        self.ensure_one()
        self.write({'state': 'endoscopy', 'endoscopy_date': fields.Datetime.now()})

    def action_post_recovery(self):
        self.ensure_one()
        self.write({'state': 'post_recovery', 'post_recovery_date': fields.Datetime.now()})

    def action_discharge(self):
        self.ensure_one()
        self.write({'state': 'dis_change', 'dis_change_date': fields.Datetime.now()})

    @api.depends('endoscopy_date', 'per_recovery_date', 'draft_date', 'post_recovery_date', 'dis_change_date')
    def _compute_durations(self):
        for record in self:
            record.to_order_duration = "Not available"
            record.to_endoscopy = "Not available"
            record.to_post_recovery = "Not available"
            record.to_discharge = "Not available"

            if record.draft_date:
                if record.per_recovery_date:
                    delta = record.per_recovery_date - record.draft_date
                    record.to_order_duration = '%d days, %d hours, %d minutes' % (
                        delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)

                if record.endoscopy_date:
                    delta = record.endoscopy_date - record.per_recovery_date
                    record.to_endoscopy = '%d hours, %d minutes, %d seconds' % (
                        delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)

                if record.post_recovery_date:
                    delta = record.post_recovery_date - record.endoscopy_date
                    record.to_post_recovery = '%d hours, %d minutes, %d seconds' % (
                        delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)

                if record.dis_change_date:
                    delta = record.dis_change_date - record.post_recovery_date
                    record.to_discharge = '%d hours, %d minutes, %d seconds' % (
                        delta.days * 24 + delta.seconds // 3600, (delta.seconds % 3600) // 60, delta.seconds % 60)
