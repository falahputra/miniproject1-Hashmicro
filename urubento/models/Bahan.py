from odoo import api, fields, models


class Bahan(models.Model):
    _name = 'urubento.bahan'
    _description = 'New Description'

    name = fields.Char(string='Nama Bahan')
    stok = fields.Integer(string='Stok')
    satuan = fields.Char(string='Satuan', default='gram')
    tgl_pembelian = fields.Date(string='Tanggal Pembelian Bahan', default = fields.Datetime.now())
    
    
    menu_ids = fields.Many2many(
        string='Menu',
        comodel_name='urubento.menu',
    )
    
    # menu_id = fields.Many2one(comodel_name='urubento.menu', string='Daftar Menu', ondelete='cascade')
    
    
    
    
    
                                        
    
    
    
