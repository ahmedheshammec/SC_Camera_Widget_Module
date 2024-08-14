# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from odoo.exceptions import UserError, ValidationError


class ResPartnerEdit(models.Model):
    _inherit = 'res.partner'

    nationality_cust = fields.Char(string="Nationality", )
    is_doctor = fields.Boolean(string='Is Doctor')
    birth_date = fields.Date(string="Date of Birth", tracking=True, )
    member_age = fields.Char(string="Full Age", store=True)
    doctor = fields.Many2one('res.partner', related="sale_order_ids.doctor_sale_id", string="Doctor")
    nationality_country_id = fields.Many2one('res.country', string='Nationality')
    gender = fields.Selection(string="Gander", selection=[('male', 'Male'), ('female', 'Female')], default='male')

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        res = super(ResPartnerEdit, self).name_search(name, args=args, operator=operator, limit=limit)

        if not res:
            partners = self.search([('phone', operator, name)] + args, limit=limit)
            res = partners.name_get()
        return res

    @api.constrains('phone')
    def _check_phone_length(self):
        for record in self:
            if record.phone and len(record.phone) != 11:
                raise ValidationError("Phone number must be 11 digits long.")

    @api.onchange('birth_date')
    def _onchange_birth_date(self):
        if self.birth_date:
            rd = relativedelta(date.today(), self.birth_date)
            self.member_age = str(rd.years) + ' Years & ' + str(rd.months) + ' Months & ' + str(
                rd.days) + ' Days'


class SaleReportDoc(models.Model):
    _inherit = 'sale.report'

    doctor_sale_id = fields.Many2one('res.partner', string="Doctor", readonly=True)


class SaleReport(models.Model):
    _inherit = 'sale.report'

    doctor_sale_id = fields.Many2one('res.partner', string="Doctor", readonly=True)

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res['doctor_sale_id'] = "s.doctor_sale_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
                s.doctor_sale_id"""
        return res
