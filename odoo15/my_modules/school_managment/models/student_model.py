from odoo import models,fields

class StudentModel(models.Model):
    _name = 'iti.student'
    name = fields.Char()