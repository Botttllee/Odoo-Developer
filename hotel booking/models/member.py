from odoo import models, fields, api

class Member(models.Model):
    _inherit = 'res.partner'
    _description = 'inherit from Customer'

    hotel_customer_ids = fields.One2many('book.hotel', 'customer_id', string='history')
    total_bookings = fields.Integer(string='Total Bookings', compute='_compute_total_bookings', store=True)

    def action_total_bookings(self):
        print(f"Total Bookings: {self.total_bookings}")
        return {
                'type': 'ir.actions.act_window',
                'name':('Total Booking'),
                'res_model': 'book.hotel',
                'view_type': 'list',
                'view_mode': 'list',
                'domain': [('customer_id', '=', self.id)],
            }
        
    @api.depends('hotel_customer_ids')
    def _compute_total_bookings(self):
        for member in self:
            member.total_bookings = len(member.hotel_customer_ids)