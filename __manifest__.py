{
    'name': 'Phone Shop',
    'description': 'Test task.',
    'author': 'Pavel Yushkevich', 
    'depends': [
        'base',
        'sale',
    ],
    'data': [
        'views/product_view.xml',
        'views/sale_view.xml',
        'views/actions.xml',
        'security/ir.model.access.csv',
        'wizard/product_wizard.xml',
    ],
    'application': False,
}