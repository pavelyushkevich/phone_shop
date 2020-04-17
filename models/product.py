from odoo import api, fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    manufacturer_id = fields.Many2one('sale.manufacturer')
    model_id = fields.Many2one('sale.manufacturer.model')

    @api.onchange('manufacturer_id')
    def onchange_manufacturer_id(self):
        if self.manufacturer_id:
            self.model_id = False
    
            
