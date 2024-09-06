from odoo import models, fields

class FasilitasHotel(models.Model):
    _name = 'fasilitas.hotel'
    _description = 'Informasi mengenai fasilitas di kamar hotel'
    _rec_name = "name_fasilitas"

    name_fasilitas = fields.Char(string="Input Nama Fasilitas")
    code_fasilitas = fields.Char(string="Input Kode Fasilitas")
    

