# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import werkzeug

from odoo import models, _


class Mailing(models.Model):
    _inherit = 'mailing.mailing'

    def action_send_statistics(self):
        return self._action_send_statistics()

    def action_unsubscribe(self):
        self.ensure_one()
        base_url = '/mailing/%s/unsubscribe' % self.id
        if self.mailing_on_mailing_list:
            document_id = self.env['mailing.contact'].search([('email_normalized', '=', self.env.user.email_normalized)]).ids[0]
        else:
            model = self.env[self.mailing_model_real]
            if 'email_normalized' in model:
                document_id = model.search([('email_normalized', '=', self.env.user.email_normalized)]).ids[0]
            elif 'email_from' in model:
                document_id = model.search([('email_from', 'ilike', self.env.user.email_normalized)]).ids[0]
            elif 'email' in model:
                document_id = model.search([('email', 'ilike', self.env.user.email_normalized)]).ids[0]
            else:
                document_id = model.search(self._parse_mailing_domain()).ids[0]

        params = werkzeug.urls.url_encode({
            'document_id': document_id,
            'email': self.env.user.email_normalized,
            'hash_token': self._generate_mailing_recipient_hash(document_id, self.env.user.email_normalized),
        })
        return {
            'type': 'ir.actions.act_url',
            'name': "Custom unsubscribe",
            'target': 'new',
            'url': '%s?%s' % (base_url, params),
        }
