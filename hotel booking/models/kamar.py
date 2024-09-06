from odoo import models, fields, api
from odoo.exceptions import ValidationError

class KamarHotel(models.Model):
    _name = 'kamar.hotel'
    _description = 'Informasi mengenai kamar hotel'

    name = fields.Char(string="Nama Kamar")
    tipe_kamar = fields.Many2one('tipe.kamar', string='tipe kamar')
    fasilitas_kamar = fields.Many2many(string='fasilitas kamar', related = "tipe_kamar.fasilitas_kamar")
    customer_id = fields.Many2one('res.partner', string='Customer')
    harga_kamar = fields.Float(string='harga kamar', related = 'tipe_kamar.harga', store=True)
    lantai = fields.Integer()
    panjang_kamar = fields.Float()
    lebar_kamar = fields.Float()
    luas_kamar = fields.Float(compute='_compute_area')
    status_kamar = fields.Boolean()
    transaksi_booking = fields.Char()
    description = fields.Text()
    
    history_ids = fields.One2many('book.hotel', 'name', string='history')


    @api.onchange('panjang_kamar', 'lebar_kamar')
    def _compute_area(self):
        for rec in self:
            rec.luas_kamar = rec.panjang_kamar * rec.lebar_kamar
