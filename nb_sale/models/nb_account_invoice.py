from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

class PaymentReceipt(models.Model):
    _inherit ='account.invoice'
    

    nomor_kwitansi = fields.Char(string='No. Kwitansi')
    untuk_2 = fields.Many2one(comodel_name='account.invoice.line', string='Untuk Pembayaran')
    
    
 

        



    
    
        
        
        
  