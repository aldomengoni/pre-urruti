# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductLifeStage(models.Model):
    _name = 'product_extra_fields.product_life_stage' # Database
    _description = 'product_extra_fields.product_life_stage'

    name = fields.Char("Nombre") # Campo Nombre de Etapa de vida
