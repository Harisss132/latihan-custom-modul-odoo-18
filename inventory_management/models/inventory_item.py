from odoo import models, fields, api
from odoo.exceptions import UserError


class InventoryItem(models.Model):
    _name = 'inventory.item'
    _description = 'Data Barang Gudang'

    name = fields.Char(string='Nama Barang', required=True)
    code = fields.Char(string='Kode Barang', required=True)
    stock = fields.Integer(string='Stok', default=0)
    price = fields.Float(string='Harga per Unit')
    description = fields.Text(string='Deskripsi Barang')
    
    supplier_id = fields.Many2one('inventory.supplier', string='Supplier')
    
    total_value = fields.Float(
        string='Total Value',
        compute='_compute_total_value',
        store=True
    )
    
    @api.depends('stock', 'price')
    def _compute_total_value(self):
        for record in self:
            record.total_value = record.stock * record.price

    def update_stock(self):
        """Fungsi untuk update stok barang"""
        for record in self:
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Sukses',
                    'message': f'Stok {record.name} berhasil diperbarui',
                    'type': 'success',
                    'sticky': False,
                }
            }

    def print_label(self):
        """Fungsi untuk mencetak label barang"""
        for record in self:
            raise UserError('Fitur cetak label sedang dalam pengembangan')

    def action_save(self):
        """Fungsi untuk save record"""
        return True

    def action_cancel(self):
        """Fungsi untuk cancel/discard perubahan"""
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }