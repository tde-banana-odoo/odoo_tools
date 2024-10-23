# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Whatsapp Tools and Helpers',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
    """,
    'depends': [
        'base_tools',
        'mail_tools',
        'whatsapp'
    ],
    'data': [
        'data/whatsapp_template.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
    'auto_install': True,
}
