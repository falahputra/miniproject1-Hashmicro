from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    tipe_pegawai = fields.Selection([
        ('chef', 'Chef'),
        ('kasir', 'Kasir'),
        ('waiters', 'Waiters')
    ], string='Tipe Pegawai')
