# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, _


class Digest(models.Model):
    _inherit = 'digest.digest'

    def action_send_preview(self):
        return self._action_send_to_user(self.env.user, tips_count=40, consum_tips=False)
