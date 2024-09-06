# -*- coding: utf-8 -*-
# from odoo import http


# class HotelBookOrder(http.Controller):
#     @http.route('/hotel_book_order/hotel_book_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_book_order/hotel_book_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_book_order.listing', {
#             'root': '/hotel_book_order/hotel_book_order',
#             'objects': http.request.env['hotel_book_order.hotel_book_order'].search([]),
#         })

#     @http.route('/hotel_book_order/hotel_book_order/objects/<model("hotel_book_order.hotel_book_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_book_order.object', {
#             'object': obj
#         })
