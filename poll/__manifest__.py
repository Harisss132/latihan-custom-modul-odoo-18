{
    'name': 'Polling',
    'version': '1.0',
    'summary': 'Polling System',
    'author': 'Ahmad Haris',
    'sequence': 10,
    'description': """Modul sederhana untuk polling""",
    'category': 'Polling/Polling',
    'depends': [],
    'data': [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/poll_views.xml",
        "views/poll_menus.xml",
    ],
    'installable': True,
    'application': True,
    'assets': {
    },
}