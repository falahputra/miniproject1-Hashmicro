from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class DetailPemesanan(models.Model):
    _name = 'urubento.detailpemesanan'
    _description = 'New Description'

    name = fields.Char(string='Name')
    pemesanan_id = fields.Many2one(comodel_name='urubento.pemesanan', string='Detail Pemesanan')
    menu_id = fields.Many2one(comodel_name='urubento.menu', string='List Menu Pesanan')
    harga_satuan = fields.Integer(string='Harga Satuan ')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    
    @api.depends('harga_satuan','qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan

    @api.onchange('menu_id')
    def _onchange_barang_id(self):
        for rec in self:
            if(self.menu_id.harga_jual):
                self.harga_satuan = self.menu_id.harga_jual
    
    # @api.model
    # def create(self,vals):
    #     record = super(DetailPenjualan,self).create(vals)
    #     if(record.qty):
    #         self.env['hasanmart.barang'].search([('id', '=', record.barang_id.id)]).write({'stok' : record.barang_id.stok - record.qty})
        # return record

    @api.constrains('qty')
    def _check_qty(self):
        for rec in self:
            if rec.qty < 1:
                raise ValidationError("Mau belanja barang {} berapa banyak sih".format(rec.menu_id.name) )
            # elif rec.menu_id.stok < rec.qty:
            #     raise ValidationError ("Menu {} tidak tersedia".format(rec.menu_id.name))
            pass

    
