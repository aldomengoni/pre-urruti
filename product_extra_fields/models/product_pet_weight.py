# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductPetWeight(models.Model):
    _name = 'product_extra_fields.product_pet_weight' # Database table
    _description = 'Peso de la Mascota / Pet Weight'

    name = fields.Char("Nombre") # Campo Nombre de Peso de la Mascota de raza contiene el intervalo
    description = fields.Text("Descripción") # Descripción