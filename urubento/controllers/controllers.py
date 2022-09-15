# -*- coding: utf-8 -*-
# from odoo import http


# class Urubento(http.Controller):
#     @http.route('/urubento/urubento', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/urubento/urubento/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('urubento.listing', {
#             'root': '/urubento/urubento',
#             'objects': http.request.env['urubento.urubento'].search([]),
#         })

#     @http.route('/urubento/urubento/objects/<model("urubento.urubento"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('urubento.object', {
#             'object': obj
#         })
