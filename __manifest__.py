# -*- coding: utf-8 -*-
##############################################################################
#
#    MJ GROUP Sp. z.o.o Managment Solution Software
#    4 Ceglana St.
#    40-514 Katowice
#
#    Copyright (C) 2019-2020 MJ Group
#
##############################################################################
{
    'name': 'Odoo Lists',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
    'summary': 'list, problems',
    'sequence': 20,
    'complexity': 'normal',
    'company': 'MJ Group Sp. z.o.o',
    'description': """
Odoo Lists
==================================
This module allows you to collect and manage customer requests. The requests are assigned to employees and their implementation is controlled.
For more information contact:\n

email: daniel.demedziuk@gmail.com

""",
    'website': 'http://www.mjgroup.pl/',
    'category': 'Tool',
    'depends': ['hr', 'mail', 'contacts'],
    'auto_install': False,
    'application': True,
    'installable': True,
    'data': [
        'security/lists_security.xml',
        'ir.model.access.csv',
        'views/lists_view.xml',
    ],
    'external_dependencies': {
    'python': [],
    },
}
