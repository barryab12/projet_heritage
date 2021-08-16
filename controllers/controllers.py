# -*- coding: utf-8 -*-
from odoo import http

# class ProjetHeritage(http.Controller):
#     @http.route('/projet_heritage/projet_heritage/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/projet_heritage/projet_heritage/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('projet_heritage.listing', {
#             'root': '/projet_heritage/projet_heritage',
#             'objects': http.request.env['projet_heritage.projet_heritage'].search([]),
#         })

#     @http.route('/projet_heritage/projet_heritage/objects/<model("projet_heritage.projet_heritage"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('projet_heritage.object', {
#             'object': obj
#         })