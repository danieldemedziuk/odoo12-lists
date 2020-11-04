#!/usr/bin/env python
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date
import logging

_logger = logging.getLogger(__name__)

today = date.today().strftime("%Y-%m-%d")


class lists_line(models.Model):
    _name = 'lists.line'
    _description = 'List of service requests'
    _order = 'id desc'

    name = fields.Char(string='Name application', required=True)
    date_request = fields.Date(string='Date', default=today)
    employee = fields.Many2one('hr.employee', string='Employee')
    applicant = fields.Char(string='Applicant', help='From whom the application was recorded.')
    project = fields.Many2one('account.analytic.account', string='Project')
    hours = fields.Float(string='Number of hours spent', help='Number of hours spent solving the problem.')
    status_icon = fields.Html(compute="_compute_status", track_visibility='onchange')
    status = fields.Selection([('0', 'Open'), ('1', 'Approved'), ('2', 'Done'), ('3', 'Cancel')], default="0", help='Current status of the case.', track_visibility='onchange', required=True)

    @api.depends("status")
    def _compute_status(self):
        icons = {"0": "fa-ticket", "1": "fa-check", "2": "fa-star", "3": "fa-times"}
        for rec in self:
            if rec.status in icons:
                rec.status_icon = "<div class='fa fa-fw %s'></div>" % icons[rec.status]
