from odoo import api ,models,fields
class AcademyProductWizards(models.TransientModel):
    _name ="academy.product.wizard"

    name=fields.Char(required=1)
    price=fields.Float(required=1)


    def action_create_product(self):
     course = self.env['academy.course'].browse(
        self.env.context.get('active_id')
     )

     product_tmpl = self.env['product.template'].create({
        'name': self.name,
        'type': 'service',
        'list_price': self.price,
        'course_id': course.id,
      })
     course.product_id = product_tmpl.product_variant_ids[0].id
     return {'type': 'ir.actions.act_window_close'}
