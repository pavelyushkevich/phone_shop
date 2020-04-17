from odoo import api, fields, models

class SaleManufacturer(models.Model):
    _name = "sale.manufacturer"
    _description = "Manufacturer"

    name = fields.Char(string="Manufacturer", required=True)

class SaleManufacturerModel(models.Model):
    _name = "sale.manufacturer.model"
    _description = "Manufacturer model"

    name = fields.Char(string="Model", required=True)
    manufacturer_id = fields.Many2one('sale.manufacturer', string="Manufacturer", required=True)