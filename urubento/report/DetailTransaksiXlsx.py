from odoo import models,fields
import datetime

class PartnerXlsx(models.AbstractModel):
    _name = 'report.urubento.report_pemesanan_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.Date.today()

    def generate_xlsx_report(self, workbook, data, pemesanan):
        sheet = workbook.add_worksheet('Daftar Penjualan')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, ("Laporan keuangan pada tanggal : "+str(self.tgl_lap)), bold)
        sheet.write(1, 0, 'No Nota', bold)
        sheet.write(1, 1, 'Nama Pembeli', bold)
        sheet.write(1, 2, 'Tgl. Transaksi', bold)
        sheet.write(1, 3, 'Jumlah Pembelian', bold)
        row = 2
        col = 0

        for obj in pemesanan:
            # report_name = obj.name
            # One sheet by partner
            col = 0
            sheet.write(row, col, obj.name, bold)
            sheet.write(row, col+1, obj.nama_pembeli, bold)
            sheet.write(row, col+2, str(obj.tgl_penjualan), bold)
            sheet.write(row, col+3, obj.total_bayar, bold)
            # for xxx in obj.barang_id:
            #     sheet.write(row, col+3, xxx.name, bold)
            #     col+=1
            row+=1