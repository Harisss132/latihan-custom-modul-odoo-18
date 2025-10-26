from odoo import models, fields

class InventorySupplier(models.Model):
    _name = "inventory.supplier"
    _description = "Inventory Supplier"
    
    name = fields.Char(string="Supplier Name", required=True)
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")
    address = fields.Text(string="Address")
    
    item_ids = fields.One2many('inventory.item', 'supplier_id', string="Items")
    