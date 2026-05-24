# from odoo import http


# class Sales-module2(http.Controller):
#     @http.route('/sales-module2/sales-module2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales-module2/sales-module2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales-module2.listing', {
#             'root': '/sales-module2/sales-module2',
#             'objects': http.request.env['sales-module2.sales-module2'].search([]),
#         })

#     @http.route('/sales-module2/sales-module2/objects/<model("sales-module2.sales-module2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales-module2.object', {
#             'object': obj
#         })

