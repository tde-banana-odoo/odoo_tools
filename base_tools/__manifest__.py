# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Base Tools and Helpers',
    'version': '1.0',
    'category': 'Tools',
    'complexity': 'easy',
    'description': """
    """,
    'depends': ['base'],
    'data': [
        'data/configuration_data.xml',
        'data/configuration_data_private.xml',  # comment me if necessary
        'data/res_company_data.xml',
        'data/res_users_data.xml',
        'data/res_partner_data_private.xml',  # comment me if necessary
        'data/ir_data.xml',
    ],
    'installable': True,
    'auto_install': False,
}
