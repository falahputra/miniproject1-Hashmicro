# -*- coding: utf-8 -*-
{
    'name': "urubento",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','report_xlsx'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/menu.xml',
        'views/bahan_view.xml',
        'views/menu_view.xml',
        'wizzard/pemesanan_wizzard_view.xml',
        'views/detailpemesanan_view.xml',
        'report/rekap_pemesanan_xlsx_view.xml',
        'views/pegawai_chef_view.xml',
        'views/pegawai_kasir_view.xml',
        'views/pegawai_waiters_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
