# -*- coding: utf-8 -*-
{
    'name': "Campos Extra (Producto)",

    'summary': "Agrega más campos al modelo Producto",

    'description': """
        Se agregan los siguientes campos:
         - Etapa de Vida
    """,

    'author': "User 01",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/life_stage_views.xml',
        'views/breed_size_views.xml',
        'views/product_extra_fields_views.xml',
        'security/ir.model.access.csv',
    ],
}
