from odoo import models

class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        res = super().action_post()

        for move in self:
            if move.move_type != 'out_invoice':
                continue

            for line in move.invoice_line_ids:
                course = line.product_id.product_tmpl_id.course_id
                if not course:
                    continue

                enrollment = self.env['academy.enrollment'].search([
                    ('student_id', '=', move.partner_id.id),
                    ('course_id', '=', course.id),
                    ('state', '=', 'draft')
                ], limit=1)

                if enrollment:
                    enrollment.write({
                        'state': 'confirmed',
                        'invoice_id': move.id
                    })
        return res
