# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductLifeStage(models.Model):
    _name = 'product_extra_fields.product_life_stage' # Database
    _description = 'Etapa de Vida / Life Stage'

    name = fields.Char("Nombre") # Campo Nombre de Etapa de vida
