# -*- coding: utf-8 -*-
from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    komisi_setting = fields.Float(string='komisi setting', config_parameter='hotel_book_order.komisi_setting')
