{
    'name': "Library Management",
    'summary': """Library management""",
    'description': """Manage a Library: customers, books, etc.... """,
    'author': "Spider4eyes",
    'website': "",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Library',
    'version': '14.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        "security/ir.model.access.csv",
        "data/library_data.xml",
    ],
    # only loaded in demonstration mode
    'demo': [],
    'license': 'AGPL-3',
}
