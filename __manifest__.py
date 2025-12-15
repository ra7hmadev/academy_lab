{
    'name': 'Academy Lab',
    'version': '18.0.1.0.0',
    'category': 'Training',
    'author': 'rahma elaa',
    'summary': 'Training Academy Management System',
    'depends': ['base', 'mail', 'contacts'],
    'data': [

        'security/academy_security.xml',
        'security/ir.model.access.csv',


        'views/enrollment_views.xml',
        'views/course_views.xml',
        'views/course_category_views.xml',
        'views/res_partner_views.xml',

           'views/academy_menu.xml',
    ],
    'application': True,
}
