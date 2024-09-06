# -*- coding: utf-8 -*-
from odoo import fields, models, api


class Team_settings(models.Model):
    _inherit = 'res.users'

    info_team = fields.Char(string = "info team", compute = '_get_sales_team')

    def _get_sales_team(self):
        if self.id:
            team = self.env['sales.team'].search([('sales_leader', '=', self.id)])
            if team:
                self.info_team = team.name
            else:
                self.info_team = "Error"