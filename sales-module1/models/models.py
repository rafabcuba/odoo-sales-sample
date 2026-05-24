# from odoo import models, fields, api


# class sales-module1(models.Model):
#     _name = 'sales-module1.sales-module1'
#     _description = 'sales-module1.sales-module1'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

