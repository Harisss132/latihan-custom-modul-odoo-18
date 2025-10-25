{
    'name': 'Inventory Management',
    'version': '1.0',
    'summary': 'Modul sederhana untuk pencatatan barang',
    'author': 'Ahmad Haris',
    'category': 'Inventory',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_item_views.xml',
    ],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'inventory_management/static/src/js/save_and_call.js',
        ],
    },
}