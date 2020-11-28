# -*- coding: utf-8 -*-
<<<<<<< HEAD
##############################################################################
#
#    MJ GROUP Sp. z.o.o Managment Solution Software
#    4 Ceglana St.
#    40-514 Katowice
#
#    Copyright (C) 2019-2020 MJ Group
#
##############################################################################
=======

>>>>>>> 5e1b0705826ff8595e2f9478fc239454f072a444
{
    'name': 'Odoo Lists',
    'version': '1.0',
    'author': 'Daniel Demedziuk',
<<<<<<< HEAD
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
=======
    'summary': 'list, requests',
    'sequence': 20,
    'complexity': 'normal',
    'company': 'Daniel Demedziuk',
    'description': """
Odoo Lists
==================================
This module allows you to collect and control service requests. All over-project requests are submitted by the implementation staff. 
This allows you to easily monitor the progress of additional work. All additional requests should be recorded here. A convenient status system makes it easy to manage requests.
For more information contact:\n

email: daniel.demedziuk@mjgroup.pl

""",
    'website': 'website',
>>>>>>> 5e1b0705826ff8595e2f9478fc239454f072a444
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
