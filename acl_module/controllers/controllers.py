# -*- coding: utf-8 -*-
# from odoo import http


# class AdvBooking(http.Controller):
#     @http.route('/adv_booking/adv_booking/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/adv_booking/adv_booking/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('adv_booking.listing', {
#             'root': '/adv_booking/adv_booking',
#             'objects': http.request.env['adv_booking.adv_booking'].search([]),
#         })

#     @http.route('/adv_booking/adv_booking/objects/<model("adv_booking.adv_booking"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('adv_booking.object', {
#             'object': obj
#         })
