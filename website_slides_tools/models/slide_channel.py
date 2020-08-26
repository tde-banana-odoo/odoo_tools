# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _


class Channel(models.Model):
    _inherit = 'slide.channel'

    def action_send_completed_mail(self):
        completed_members = self.channel_partner_ids.filtered('completed')
        return completed_members._send_completed_mail()
