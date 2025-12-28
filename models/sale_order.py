from odoo import api , fields ,models
class SaleOrder(models.Model):
     _inherit = 'sale.order'

     def action_confirm(self):
          res =super().action_confirm()

          for order in self:
            for line in order.order_line:
                course = line.product_id.product_tmpl_id.course_id
                if not course:
                    continue
            
                exists = self.env['academy.enrollment'].search([
                    ('student_id', '=', order.partner_id.id),
                    ('course_id', '=', course.id)
                ], limit=1)

                if not exists:
                    self.env['academy.enrollment'].create({
                        'student_id': order.partner_id.id,
                        'course_id': course.id,
                        'state': 'draft',
                    })
          return res   

     
     


