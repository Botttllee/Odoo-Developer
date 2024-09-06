from odoo import models, fields, api

class TipeKamar(models.Model):
    _name = 'tipe.kamar'
    _description = 'Informasi tentang tipe kamar'
    _rec_name = "name_tipe"

    name_tipe = fields.Char(string="Tipe Kamar")
    fasilitas_kamar = fields.Many2many('fasilitas.hotel', string='fasilitas kamar')
    harga = fields.Float(string='Input Harga Kamar')
    