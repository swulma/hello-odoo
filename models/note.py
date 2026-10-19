
from odoo import models, fields


class Note(models.Model):
    _name = "hello.odoo.note"
    _description = "Note Management"

    title = fields.Char(string="Title", required=True)

    content = fields.Text(string="Content")

    date = fields.Datetime(string="Created On", default=fields.Datetime.now)
