# hotel_book_order.access_sales_team_model,access_sales_team_model,hotel_book_order.model_sales_team_model,base.group_user,1,1,1,1

from odoo import models, fields, api

class SalesTeam(models.Model):
    _name = 'sales.team'
    _description = 'Sales Team Information'

    name = fields.Char(string='Nama Sales Team', required=True)
    total_transaksi = fields.Float(string='Total Transaksi', compute='_compute_total_transaksi')
    total_komisi = fields.Float(string='Total Komisi', compute='_compute_total_komisi')
    sales_leader = fields.Many2one('res.users', string='Sales Leader', domain=lambda self: [('groups_id', '=', self.env.ref('hotel_book_order.group_supervisor').id)])
    sales_persons = fields.Many2many('res.users', string='Sales Persons', domain=lambda self: [('groups_id', '=', self.env.ref('hotel_book_order.group_user').id)])

    def _compute_total_transaksi(self):
        for team in self:
            total_transaksi = 0.0
            for sales_person in team.sales_persons:
                transactions = self.env['book.hotel'].search([('orang_sales', '=', sales_person.id)])
                total_transaksi += sum(transactions.mapped('total_harga_kamar'))
            team.total_transaksi = total_transaksi

    def _compute_total_komisi(self):
        for team in self:
            print("test total komisi")
            commission_percentage = self.env['ir.config_parameter'].sudo().get_param('hotel_book_order.komisi_setting')
            print("Komisi: ", commission_percentage)   
            commission_percentage_float = float(commission_percentage)  
            print("Komisi: ", commission_percentage_float) 
            commission_percentage_str = '{:.0%}'.format(commission_percentage_float / 100) 
            print("Komisi: ", commission_percentage_str)      
            team.total_komisi = team.total_transaksi * commission_percentage_float / 100        