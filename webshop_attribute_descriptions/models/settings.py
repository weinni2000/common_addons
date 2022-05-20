# -*- coding: utf-8 -*-

from odoo import models, fields, api, modules
import io
import base64
import os
from bs4 import BeautifulSoup


class settings(models.TransientModel):
    _inherit = "res.config.settings"  # -*- coding: utf-8 -*-

    additional_information = fields.Boolean(
        string='Extensible Information on Website', help="What's your Account used to retrieve Posts")

    def set_values(self):
        res = super(settings, self).set_values()
        self.env["ir.config_parameter"].set_param(
            "webshop_attribute_descriptions.additional_information", self.additional_information)
        return res

    @api.model
    def get_values(self):
        res = super(settings, self).get_values()
        ICPSudo = self.env["ir.config_parameter"].sudo()
        additional_information = ICPSudo.get_param(
            "webshop_attribute_descriptions.additional_information")
        res.update(additional_information=additional_information)
        return res


class Website(models.Model):
    _inherit = "website"  # -*- coding: utf-8 -*-

    show_category_info = fields.Boolean()
    show_attribute_info = fields.Boolean()
