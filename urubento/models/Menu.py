from odoo import api, fields, models


class Menu(models.Model):
    _name = 'urubento.menu'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_jual = fields.Integer(string='Harga', required = True)


    
    # bahan_ids = fields.Many2many(
    #     string='Bahan',
    #     comodel_name='urubento.bahan',
    # )
    
    
    bahan_ids = fields.Many2many(
        string='Daftar Bahan',
        comodel_name='urubento.bahan',
    )
    
    @api.depends('bahan_ids')
    def _compute_bahan_ids(self):
        for rec in self:
            a = self.env['urubento.bahan'].search([('menu_ids','=',rec.id)]).mapped('name')
            # b = len(a)
            # rec.jml_item = b    
            rec.daftar = a
    daftar = fields.Char(compute = '_compute_bahan_ids',string='Daftar Bahan')
