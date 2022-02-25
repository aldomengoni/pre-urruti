# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductColor(models.Model):
    _name = 'product_extra_fields.product_color' # Database table

    name = fields.Char("Nombre") # Campo Nombre de Color
    description = fields.Text("Decripción") # Intervalo de medida