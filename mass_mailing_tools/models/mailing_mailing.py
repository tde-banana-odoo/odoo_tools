# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _


class Mailing(models.Model):
    _inherit = 'mailing.mailing'

    def action_send_statistics(self):
        return self._action_send_statistics()
