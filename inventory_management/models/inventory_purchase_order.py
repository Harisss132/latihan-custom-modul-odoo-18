from odoo import models, fields, api

class InventoryPurchaseOrder(models.Model):
    _name = 'inventory.purchase.order'
    _description = 'Inventory Purchase Order'
    _rec_name = 'reference'
    
    reference = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, 
                            default=lambda self: 'New'  )
    supplier_id = fields.Many2one('inventory.supplier', string='Supplier', required=True)
    order_date = fields.Date(string='Order Date', default=fields.Date.today)
    order_line_ids = fields.One2many('inventory.purchase.order.line', 'order_id', string='Order Lines')
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    
    @api.depends('order_line_ids.subtotal')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = sum(line.subtotal for line in record.order_line_ids)
    
    @api.model
    def create(self, vals):
        if vals.get('reference', 'New') == 'New':
            # use the correct ir.sequence model (typo fixed)
            vals['reference'] = self.env['ir.sequence'].next_by_code('inventory.purchase.order') or 'New'
        return super().create(vals)
    
class InventoryPurchaseOrderLine(models.Model):
    _name = 'inventory.purchase.order.line'
    _description = 'Inventory Purchase Order Line'
    
    order_id = fields.Many2one('inventory.purchase.order', string='Order Reference', ondelete='cascade')
    product_id = fields.Many2one('inventory.item', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', default=1)
    price_unit = fields.Float(string='Unit Price', required=True)
    subtotal = fields.Float(string='Subtotal', compute='_compute_subtotal', store=True)
    
    @api.depends('quantity', 'price_unit')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.quantity * line.price_unit
    
    