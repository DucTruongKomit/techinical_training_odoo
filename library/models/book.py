from odoo import fields, models

class Book(models.Model):
    _name = "book"

    name = fields.Char(string="Name of Book")
    author = fields.Many2one()
    editors = fields.Many2many()
    edition_year = fields.Integer()

