# -*- coding: utf-8 -*-

from odoo import api, fields, models, _, api
from odoo.exceptions import ValidationError
from pytz import utc
import pytz


class ProductAttribute(models.Model):
    _inherit = "product.attribute"

    description_website = fields.Char()


class ProductAttributeValue(models.Model):
    _inherit = "product.attribute.value"

    description_website = fields.Char()


class ProductAttributeValue(models.Model):
    _inherit = "product.category"

    description_website = fields.Char()
