{
    'name': "Module Custom Pembelian",
    'version': '1.0',
    'author': "Khoerul Mutaqin",
    'category': 'Purchase',
    'description': """
    Description text
    """,

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/algoritma_pembelian_menuitem.xml',
        'views/algoritma_pembelian_views.xml',
        # 'views/algoritma_pembelian_action.xml',
        


    ],


    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    # 'installable': True,
    # 'application': True
}
