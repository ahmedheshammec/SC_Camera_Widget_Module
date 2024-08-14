# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Process(models.Model):
    _name = 'process.name'
    _description = 'Process Description'

    name = fields.Char(string='Process Name', required=True)
    detail = fields.Text(string='Process Detail')
    medical_process_id = fields.Many2one('medical.endoscopes', string='Related Endoscope')
