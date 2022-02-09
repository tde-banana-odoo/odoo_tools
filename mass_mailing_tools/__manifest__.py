# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Email Marketing Tools and Helpers',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
    """,
    'depends': [
        'mail_tools',
        'mass_mailing',
    ],
    'data': [
        'views/mailing_mailing_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
