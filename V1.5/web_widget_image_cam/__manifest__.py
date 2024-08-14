# -*- coding: utf-8 -*-

{
    'name': 'Image WebCam Widget',
    'version': '1.0',
    'category': 'Tool',
    'sequence': 6,
    'license': "LGPL-3",
    'author': 'ErpMstar Solutions',
    'summary': "Allow you to capture image from your webcam in image widget.",
    'description': "Allow you to capture image from your webcam in image widget.",
    'depends': ['base', 'web', 'sales_doctor'],
    'data': [
        'security/ir.model.access.csv',
        'data/medical_sequence.xml',
        'view/medical_endoscopes.xml',
        # 'view/medical_action_report.xml',
        # 'reports/report_medical.xml',
        # 'reports/photo_medical.xml',
    ],

    'assets': {
        'web.assets_backend': [
            '/web_widget_image_cam/static/src/js/widget.js',
            '/web_widget_image_cam/static/src/js/webcam.js',
            '/web_widget_image_cam/static/src/js/SaveRecord.js',
            '/web_widget_image_cam/static/src/js/RecordRTC.js',
            '/web_widget_image_cam/static/src/css/widget.css',
            '/web_widget_image_cam/static/src/css/custom.scss',
            '/web_widget_image_cam/static/src/xml/widget.xml',

        ],
    },

    'images': [
        'static/description/icon.png',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'price': 10,
    'currency': 'EUR',
}
