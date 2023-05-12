from odoo import api, fields, models, exceptions


class Progress(models.Model):
    _name = 'arisnew.progress'
    _inherit = 'mail.thread'
    _description = 'Progress'

    no = fields.Integer(string='No', track_visibility='onchange')

    deskripsi = fields.Html(string='Description', track_visibility='onchange')

    pic = fields.Char(string='Pic', track_visibility='onchange')

    tag_ids = fields.Many2many('project.tags', string='Tags')

    tgl_awal = fields.Date(
        string='Tanggal awal',
        default=fields.Datetime.now(),
        track_visibility='onchange')

    do_that = fields.Char(string='Do that', track_visibility='onchange')

    tgl_akhir = fields.Date(
        string='Tanggal Akhir',
        default=fields.Datetime.now(),
        track_visibility='onchange')

    progress = fields.Integer(string='Progress',  track_visibility='onchange')

    taken_seats = fields.Float(
        compute='_compute_taken_seats',
        string='Progress',
        store=True,
    )

    state = fields.Selection(string='State', selection=[
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ],  readonly=True, default='draft', required=True, track_visibility='onchange')

    def action_confirm(self):
        # validasi
        # manipulasi
        # rubah state ke confirm
        self.write({'state': 'confirm'})

    def action_done(self):
        # validasi
        # manipulasi
        # rubah state ke done
        self.write({'state': 'done'})

    def action_cancel(self):
        # validasi
        # manipulasi
        # rubah state ke cancel
        self.write({'state': 'cancel'})

    def action_draft(self):
        # validasi
        # manipulasi
        # rubah state ke draft
        self.write({'state': 'draft'})

    def action_Reset(self):
        # validasi
        # manipulasi
        # rubah state ke draft
        self.write({'state': 'draft'})

        # @api.multi

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise exceptions.UserError('tidak bisa hapus data selain draft')
        return super(Progress, self).unlink()

    @api.depends('progress')
    def _compute_taken_seats(self):
        for record in self:
            if not record.progress:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * record.progress / 100

    class ProjectTags(models.Model):
        """ Tags of project's tasks """
        _name = "project.tags"
        _description = "Project Tags"

        name = fields.Char('Tag Name', required=True)
        color = fields.Integer(string='Color Index')

        _sql_constraints = [
            ('name_uniq', 'unique (name)', "Tag name already exists!"),
        ]
