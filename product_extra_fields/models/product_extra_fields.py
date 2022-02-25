# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProductExtraFields(models.Model):
    _inherit = 'product.template' # Modelo heredado

    life_stage = fields.Many2one("product_extra_fields.product_life_stage", string="Etapa de vida")
    breed_size = fields.Many2one("product_extra_fields.product_breed_size", string="Tamaño de raza")
    size = fields.Many2one("product_extra_fields.product_size", string="Talla")
    color = fields.Many2one("product_extra_fields.product_color", string="Color")
    pet_weight = fields.Many2one("product_extra_fields.product_pet_weight", string="Peso de la Mascota")
    influencer = fields.Many2one("product_extra_fields.product_influencer", string="Influencer")

    # Entregas
    # -- Entrega en tienda
    en_tienda = fields.Selection([
        ('0','No'),
        ('1','Si')], string='Entrega en tienda', required=True, default='1')
    # -- Delivery mismo día
    deliv_mismo = fields.Selection([
        ('0','No'),
        ('1','Si')], string='Delivery mismo día', required=True, default='0')
    # -- Delivery programado
    deliv_program = fields.Selection([
        ('0','No'),
        ('1','Si')], string='Delivery programado', required=True, default='0')
    # -- Permite Suscripción
    suscrp = fields.Selection([
        ('0','No'),
        ('1','Si')], string='Permite suscripción', required=True, default='0')
