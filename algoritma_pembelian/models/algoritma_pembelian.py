# -*- coding: utf-8 -*-

from odoo import fields, models


class algoritma_pembelian(models.Model):
    _name = 'algoritma.pembelian'
#    _description = 'Data Course'

    name    = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status  = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('done', 'Done')
    ])
