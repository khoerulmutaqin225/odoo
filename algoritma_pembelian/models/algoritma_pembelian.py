# -*- coding: utf-8 -*-

from odoo import fields, models


class algoritma_pembelian(models.Model):
    _name = 'algoritma.pembelian'
    #  _description = 'Data Course'

    name    = fields.Char(string="Name")
    tanggal = fields.Date(string="Tanggal")
    status  = fields.Selection([(
        'draft', 'Draft'),
        ('on_procces', 'On Procces'),
        ('to_approve', 'To Approve'),
        ('done', 'Done')], default='draft')
    # algoritma_pembelajaran_ids = fields.One2many('algoritma.pembelian.line', 'algoritma_pembelian_line', string='')
    

# class algoritma_pembelian_line(models.Model):
#     _name :'algoritma.pembelian.line'

#     algoritma_pembelian_id = fields.Many2one('algoritma.pembelian', string="Algoritma Pembelian Id")
#     product_id  = fields.Many2one('product.product', string="Product Id")
#     quantity  = fields.Float(string= "Quantity",default=0.0)
#     uom_id = fields.Many2one('uom.uom',string="Uom Id")


