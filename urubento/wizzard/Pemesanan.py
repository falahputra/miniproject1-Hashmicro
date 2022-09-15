from odoo import api, fields, models


class Pemesanan(models.Model):
    _name = 'urubento.pemesanan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(string ='Tgl. Transaksi' , default = fields.Datetime.now())
    total_bayar = fields.Integer(compute = '_compute_totalbayar',string='Total Pembayaran')
    detailpemesanan_ids = fields.One2many(
        comodel_name='urubento.detailpemesanan', 
        inverse_name='pemesanan_id', 
        string='Detail Pemesanan')


    # menu_id = fields.Many2one(
    #     string='Nama Menu',
    #     comodel_name='urubento.menu',
    #     required=True,
    # )
    @api.depends('detailpemesanan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['urubento.detailpemesanan'].search([('pemesanan_id','=',rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    jumlah = fields.Integer(string='Jumlah', required = False)
    
    def button_pesanan(self):
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


