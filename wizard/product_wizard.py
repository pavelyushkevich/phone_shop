from odoo import api, fields, models

class ProductTemplateWizard(models.TransientModel):
    _name = "product.template.wizard"

    name = fields.Char('Name', required=True, compute='compute_name')
    type = fields.Selection([('consu', 'Consumable'), ('service', 'Service')], string='Product Type', default='consu', required=True)
    categ_id = fields.Many2one('product.category', 'Product Category', required=True)
    sale_ok = fields.Boolean('Can be Sold', default=True)
    purchase_ok = fields.Boolean('Can be Purchased', default=True)
    default_code = fields.Char('Internal Reference')
    barcode = fields.Char('Barcode')
    manufacturer_id = fields.Many2one('sale.manufacturer')
    model_id = fields.Many2one('sale.manufacturer.model')
    image_medium = fields.Binary("Medium-sized image", attachment=True)
    state = fields.Selection([('step1', 'step1'),('step2', 'step2')], default='step2')
    change_step = fields.Boolean()

    @api.multi
    @api.onchange('change_step')
    def onchange_change_step(self):
        for record in self:
            if record.state == 'step1':
                record.state = 'step2'
            else:
                record.state = 'step1'

    @api.onchange('manufacturer_id')
    def onchange_manufacturer_id(self):
        if self.manufacturer_id:
            self.model_id = False

    @api.onchange('model_id')
    def compute_name(self):
        if self.model_id:
            self.name = str(self.manufacturer_id.name) + ' - ' + str(self.model_id.name)

    def create_product(self):
        vals = {
            'name': self.name,
            'type': self.type,
            'categ_id': self.categ_id.id,
            'sale_ok': self.sale_ok,
            'purchase_ok': self.purchase_ok,
            'default_code': self.default_code,
            'barcode': self.barcode,
            'manufacturer_id': self.manufacturer_id.id,
            'model_id': self.model_id.id,
            'image_medium': self.image_medium,
        }
        self.env['product.template'].create(vals)
