# -*- coding: utf-8 -*-
{
    'name': 'Webshop Attribute Descriptions',
    'version': '15.1',
    'summary': 'Webshop Attribute Descriptions',
    'sequence': -100,
    'description': """Webshop Attribute Descriptions""",
    'category': 'Productivity',
    'author': 'weinni2000',
    'maintainer': 'weinni2000',
    'website': 'https://www.mytime.click',
    'license': 'AGPL-3',
    'depends': ["product", "website_sale", "base", "sale"
                ],
    'data': [
        # 'security/ir.model.access.csv',
        # 'data/sequence.xml',
        'views/attribute_extender_view.xml',
        'views/website_extender.xml',
        'views/special_settings.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
