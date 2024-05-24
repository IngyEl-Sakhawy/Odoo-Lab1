# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Products(models.Model):
    _name = 'products'
    _description = 'Products'

    name = fields.Char(string="Product Name")
    cost = fields.Float(string="Cost")
    description = fields.Text(string="Description")
    quantity = fields.Integer(string="Quantity")
    barcode = fields.Char(string="Barcode")
    category = fields.Many2one('product.category', string="Category")


