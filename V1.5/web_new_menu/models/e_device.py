# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NewModule(models.Model):
    _inherit = 'medical.endoscopes'

    e_device_ids = fields.Many2one('e.device', string='Scope Number')
    process_name = fields.Selection(string="Process Name",
                                    selection=[('upper', 'Upper Endoscopy'), ('eus', 'EUS'),
                                               ('ercp', 'ERCP'), ('colonoscopy', 'Colonoscopy'), ], default='upper')
    process_ids = fields.Many2one('process.name', string='Process Name', invisible=True)
    process_name_display = fields.Char(compute='_compute_process_name_display')

    # New fields specific to 'Upper Endoscopy'
    esophagus = fields.Text(string="Esophagus")
    stomach = fields.Text(string="Stomach")
    pylorus = fields.Text(string="Pylorus")
    duodenum = fields.Text(string="Duodenum")

    # New field specific to 'EUS'
    pancreas = fields.Text(string="Pancreas")

    # New field specific to 'ERCP'
    papilla = fields.Text(string="Papilla")

    # New field specific to 'colonoscopy'
    colon = fields.Text(string="Colon")
    referring = fields.Text(string="Referring Doctor")

    @api.depends('process_name')
    def _compute_process_name_display(self):
        selection_dict = dict(self._fields['process_name'].selection)
        for record in self:
            record.process_name_display = selection_dict.get(record.process_name, '')


class EDevice(models.Model):
    _name = 'e.device'
    _description = 'Electronic Device'

    name = fields.Char(string='Device Name', required=True)
    code = fields.Char(string='Device Code', )
    medical_endoscope_id = fields.Many2one('medical.endoscopes', string='Related Endoscope')
    device_line_ids = fields.One2many('e.device.line', 'e_device_id', string='Maintenance Lines')


class EDeviceLine(models.Model):
    _name = 'e.device.line'
    _description = 'Electronic Device Line'

    e_device_id = fields.Many2one('e.device', string='Related Device')
    malfunction = fields.Char(string='العطل')
    malfunction_date = fields.Date(string='تاريخ العطل')
    malfunction_type = fields.Text(string='نوع العطل')
    sent_for_maintenance = fields.Date(string='تاريخ ارسال للصيانة')
    back_from_maintenance = fields.Date(string='والعودة من الصيانة')
    fixed_issues = fields.Text(string='ما تم اصلاخة')
    maintenance_company = fields.Char(string='اسم شركة الصيانة')
    maintenance_cost = fields.Float(string='التكلفة')
    note = fields.Text(string='ملاحظات')
