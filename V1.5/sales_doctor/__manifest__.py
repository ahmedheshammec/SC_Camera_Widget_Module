# -*- coding: utf-8 -*-
{
    'name': "sales_doctor",
    'summary': """    """,
    'description': """   """,
    'author': "Abd El-hamed Saad",
    'website': "http://www.MyCompany.co",
    'category': 'Uncategorized',
    'version': '0.16',
    'license': "AGPL-3",

    'depends': ['base', 'sale_management', 'sale', 'stock', 'sale_stock', 'account', 'mail', 'purchase',],

    'data': [
        # 'security/ir.model.access.csv',

        'views/sale_order_inh_view.xml',
        'views/stock_picking_view.xml',
        'views/account_payment.xml',
        'report/templates.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 10,
    'currency': 'EUR',
}
