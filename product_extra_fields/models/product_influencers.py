# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductInfluencer(models.Model):
    _name = 'product_extra_fields.product_influencer' # Database table
    _description = 'Influencer / Influencer'

    name = fields.Char("Nombre")  # Campo Nombre de Influencer
    # description = fields.Text("Descripción")  # Descripción