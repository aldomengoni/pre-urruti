# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductSize(models.Model):
    _name = 'product_extra_fields.product_size' # Database table
    _description = 'Talla / Size'

    name = fields.Char("Nombre") # Campo Nombre de Talla
    intervalo = fields.Char("Tamaño de Talla") # Intervalo de medida