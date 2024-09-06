# -*- coding: utf-8 -*-
{
    'name': "Hotel book order",
    'version': '1.0.0',
    'category':"Hotel",
    'summary':"Book a hotel now",
    'description':"Booking a hotel",
    'author': "Hendrik",
    'website': "http://www.yourcompany.com",
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'sequence':-1000,
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',   
        'views/views_kamar.xml',   
        'views/views_fasilitas.xml',  
        'views/views_transaksi.xml',  
        'views/views_tipe.xml',
        'views/views_member.xml',
        # 'views/views_res.users.xml',
        'views/views_res_config_settings.xml',
        'views/views_sales.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
