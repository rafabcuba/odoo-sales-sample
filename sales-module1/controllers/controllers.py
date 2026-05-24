# from odoo import http


# class Sales-module1(http.Controller):
#     @http.route('/sales-module1/sales-module1', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales-module1/sales-module1/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales-module1.listing', {
#             'root': '/sales-module1/sales-module1',
#             'objects': http.request.env['sales-module1.sales-module1'].search([]),
#         })

#     @http.route('/sales-module1/sales-module1/objects/<model("sales-module1.sales-module1"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales-module1.object', {
#             'object': obj
#         })

