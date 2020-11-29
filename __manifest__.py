# -*- coding: utf-8 -*-
{
    'name': 'Odoo Lists',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
    'summary': 'list, problems',
    'sequence': 20,
    'complexity': 'normal',
    'company': 'Daniel Demedziuk',
    'description': """
Odoo Lists
==================================
This module allows you to collect and control service requests. All over-project requests are submitted by the implementation staff.
This allows you to easily monitor the progress of additional work. All additional requests should be recorded here. A convenient status system makes it easy to manage requests.
For more information contact:\n

email: daniel.demedziuk@gmail.com
""",
    'website': 'website',
    'category': 'Tool',
    'depends': ['hr', 'mail', 'project'],
    'auto_install': False,
    'application': True,
    'installable': True,
    'data': [
        'security/lists_security.xml',
        'security/ir.model.access.csv',
        'views/lists_view.xml',
    ],
    'external_dependencies': {
    'python': [],
    },
}
