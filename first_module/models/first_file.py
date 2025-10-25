from odoo import models, fields, api, _
from odoo.exceptions import UserError

class CustomModel(models.Model):
    _name = 'custom.model'
    _description = 'Custom Model'
    
    name = fields.Char(string='Name', required=True)
    description = fields.Char(string='Description')
    
    def action_save(self):
        """ Fungsi untuk save record """
        return True
    
    def action_cancle(self):
        """ Fungsi untuk cancle/discard perubahan """
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }