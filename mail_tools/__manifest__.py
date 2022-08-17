# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Mail Tools and Helpers',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
    """,
    'depends': [
        'base_tools',
        'mail'
    ],
    'data': [
        'data/configuration_data.xml',
        'data/configuration_data_private.xml',  # comment if necessary
    ],
    'installable': True,
    'license': 'LGPL-3',
    'auto_install': True,
}
