from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelAppointment(models.Model):
    _name = 'book.hotel'
    _description = 'Booking a hotel in this app'

    STATUS_SELECTION = [
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('finish', 'Finish'),
        ('cancel', 'Cancel'),
    ]

    name = fields.Many2one('kamar.hotel', string='nama kamar')
    tipe_kamar = fields.Many2one(related="name.tipe_kamar")
    fasilitas_kamar = fields.Many2many(related='tipe_kamar.fasilitas_kamar')
    customer_id = fields.Many2one('res.partner', string='Customer')
    checkin_date = fields.Date(string='Check-In Date')
    checkout_date = fields.Date(string='Check-Out Date')
    harga_kamar = fields.Float(string='harga kamar', related='tipe_kamar.harga', store=True)
    status = fields.Selection(STATUS_SELECTION, string='Status', default='draft')
    duration = fields.Integer(string='Duration', compute='_compute_duration', store=True)
    note = fields.Text(string='Note')

    order_id = fields.Char(string='Order ID', readonly=True, copy=False)

    @api.model
    def create(self, values):
        if values.get('order_id', '/') == '/':
            values['order_id'] = self.env['ir.sequence'].next_by_code('book.hotel.sequence') or '/'
        return super(HotelAppointment, self).create(values)    
    
    _sql_constraints = [
        ('order_id_unique', 'unique(order_id)', 'Order ID must be unique!'),
    ]    

    @api.depends('checkin_date', 'checkout_date')
    def _compute_duration(self):
        for appointment in self:
            if appointment.checkin_date and appointment.checkout_date:
                duration = (appointment.checkout_date - appointment.checkin_date).days
                appointment.duration = duration if duration >= 0 else 0
            else:
                appointment.duration = 0

    def _check_overlapping_bookings(self, date):
        overlapping_bookings = self.env['book.hotel'].search([
            ('name', '=', self.name.id),
            ('checkin_date', '<=', date),
            ('checkout_date', '>', date),
            ('status', '=', 'active'),
        ])
        if overlapping_bookings:
            raise ValidationError("The room is already booked on the selected date.")

    @api.onchange('checkin_date', 'checkout_date')
    def _onchange_booking_dates(self):
        if self.checkin_date and self.checkout_date:
            if self.checkout_date < self.checkin_date:
                raise ValidationError("Checkout Cannot be smaller than Checkin")
        for rec in self:
            if rec.checkin_date and rec.checkout_date:
                rec._check_overlapping_bookings(rec.checkin_date)
                rec._check_overlapping_bookings(rec.checkout_date)

    def confirm_transaction(self):
        for appointment in self:
            # Cek kamar nya berdasarkan tanggal
            appointment._check_overlapping_bookings(appointment.checkin_date)
            appointment._check_overlapping_bookings(appointment.checkout_date)
            print("test")
            # Update status kamar nya
            appointment.name.write({'status_kamar': True})  # assuming 'status_kamar' is the correct field

            # Confirm the transaction
            appointment.status = 'active'
