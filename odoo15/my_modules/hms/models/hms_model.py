from odoo import models,fields

class Hospitals(models.Model):
    _name ='hms.patient'
    FirsName=fields.Char()
    LastName=fields.Char()
    BirthDate=fields.Char()
    CRRatio=fields.Float()
    Bloodtype=fields.Selection([('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    PCR=fields.Boolean()
    Image=fields.Image()
    Address=fields.Text()
    Age=fields.Integer()
    state = fields.Selection([ ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious')],string='State', default='undetermined')
    departemnt_id=fields.Many2one('hms.department', string='Department')
    doctors_id=fields.Many2many('hms.doctors', string='Doctors')
    History=fields.Char(string='History')

class Department(models.Model):
    _name = "hms.department"

    name = fields.Char(string='Department Name')
    capacity = fields.Integer(string='Department Capacity')
    is_opened = fields.Boolean(string='Is Opened')
    pateints_id = fields.One2many('hms.patient', 'departemnt_id', string='Pateints')

class Doctors(models.Model):
    _name='hms.doctors'
    firstname=fields.Char()
    lastname=fields.Char()
    images=fields.Image()