from odoo import models, fields, api
from odoo.exceptions import ValidationError

class AcademyProductWizard(models.TransientModel):
    _name = 'academy.product.wizard'
    _description = 'Academy Product Wizard'
    
    name = fields.Char(string='Product Name', required=True)
    price = fields.Float(string='Price', required=True)
    course_id = fields.Many2one('academy.course', string='Course')
    
    def action_create_product(self):
        self.ensure_one()
        
        if self.price <= 0:
            raise ValidationError('Price must be greater than zero')
        
        product = self.env['product.product'].create({
            'name': self.name,
            'type': 'service',
            'list_price': self.price,
            'course_id': self.course_id.id,
            'sale_ok': True,
            'purchase_ok': False,
        })
        
        self.course_id.write({
            'product_id': product.id
        })
        
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Product Created',
                'message': f'Product "{self.name}" has been created successfully',
                'type': 'success',
                'sticky': False,
            }
        }