# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductBreedSize(models.Model):
    _name = 'product_extra_fields.product_breed_size' # Database table

    name = fields.Char("Nombre") # Campo Nombre de Tamano de raza
    intervalo = fields.Char("Intervalo de tamaño") # Intervalo de medida