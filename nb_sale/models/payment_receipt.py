from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PaymentReceiptNB(models.Model):
    _name = 'payment.receipt.nb'

    no_kwitansi = fields.Char(string='Payment Receipt Number')
    no_po = fields.Char(string='PO Number')
    jumlah = fields.Char(string='Amount')
    bilangan = fields.Char(string='Terbilang')
    partner_id = fields.Many2one(comodel_name='res.partner', string='Customer')
    untuk = fields.Many2one(comodel_name='product.product', string='Untuk Pembayaran')