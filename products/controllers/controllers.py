# -*- coding: utf-8 -*-
# from odoo import http


# class CoursesSystem(http.Controller):
#     @http.route('/courses_system/courses_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/courses_system/courses_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('courses_system.listing', {
#             'root': '/courses_system/courses_system',
#             'objects': http.request.env['courses_system.courses_system'].search([]),
#         })

#     @http.route('/courses_system/courses_system/objects/<model("courses_system.courses_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('courses_system.object', {
#             'object': obj
#         })

