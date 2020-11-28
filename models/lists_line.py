#!/usr/bin/env python
# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from datetime import date
import logging

_logger = logging.getLogger(__name__)
# _logger.info(zmienna)

today = date.today().strftime("%Y-%m-%d")

class lists_line(models.Model):
    _name = 'lists.line'
    _description = 'List of service requests'
    _order = 'id desc'

    name = fields.Char(string='Nazwa zgłoszenia', required=True)
    date_request = fields.Date(string='Data zgłoszenia', default=today)
    employee = fields.Many2one('hr.employee', string='Pracownik')
    applicant = fields.Char(string='Zgłaszający', help='Od kogo zostało zanotowane zgłoszenie.')
    project = fields.Many2one('account.analytic.account', string='Projekt')
    hours = fields.Float(string='Ilość poświęconych godzin', help='Ilość poświęconych godzin na rozwiązanie problemu.')
    status_icon = fields.Html(compute="_compute_status", track_visibility='onchange')
    status = fields.Selection([('0', 'Otwarte'), ('1', 'Zatwierdzone'), ('2', 'Ukończone'), ('3', 'Anulowane')], default="0", help='Aktualny status sprawy.', track_visibility='onchange', required=True)

    @api.depends("status")
    def _compute_status(self):
        icons = {"0": "fa-ticket", "1": "fa-check", "2": "fa-star", "3": "fa-times"}
        for rec in self:
            if rec.status in icons:
                rec.status_icon = "<div class='fa fa-fw %s'></div>" % icons[rec.status]
