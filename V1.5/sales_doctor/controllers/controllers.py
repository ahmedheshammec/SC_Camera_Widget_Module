# -*- coding: utf-8 -*-
# from odoo import http


# class SalesDoctor(http.Controller):
#     @http.route('/sales_doctor/sales_doctor', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_doctor/sales_doctor/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_doctor.listing', {
#             'root': '/sales_doctor/sales_doctor',
#             'objects': http.request.env['sales_doctor.sales_doctor'].search([]),
#         })

#     @http.route('/sales_doctor/sales_doctor/objects/<model("sales_doctor.sales_doctor"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_doctor.object', {
#             'object': obj
#         })
