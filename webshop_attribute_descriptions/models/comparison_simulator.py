from collections import OrderedDict

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    def _prepare_categories_for_display(self):
        """On the comparison page group on the same line the values of each
        product that concern the same attributes, and then group those
        attributes per category.

        The returned categories are ordered following their default order.

        :return: OrderedDict [{
            product.attribute.category: OrderedDict [{
                product.attribute: OrderedDict [{
                    product: [product.template.attribute.value]
                }]
            }]
        }]
        """
        attributes = self.product_tmpl_id.valid_product_template_attribute_line_ids._without_no_variant_attributes().attribute_id.sorted()
        categories = OrderedDict([(cat, OrderedDict())
                                 for cat in attributes.category_id.sorted()])
        if any(not pa.category_id for pa in attributes):
            # category_id is not required and the mapped does not return empty
            categories[self.env['product.attribute.category']] = OrderedDict()
        for pa in attributes:
            categories[pa.category_id][pa] = OrderedDict([(
                product,
                product.product_template_attribute_value_ids.filtered(
                    lambda ptav: ptav.attribute_id == pa)
            ) for product in self])

        return categories


class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    def _prepare_categories_for_display(self):
        """On the product page group together the attribute lines that concern
        attributes that are in the same category.

        The returned categories are ordered following their default order.

        :return: OrderedDict [{
            product.attribute.category: [product.template.attribute.line]
        }]
        """
        attributes = self.attribute_id
        categories = OrderedDict([(cat, self.env['product.template.attribute.line'])
                                 for cat in attributes.category_id.sorted()])
        if any(not pa.category_id for pa in attributes):
            # category_id is not required and the mapped does not return empty
            categories[self.env['product.attribute.category']
                       ] = self.env['product.template.attribute.line']
        for ptal in self:
            categories[ptal.attribute_id.category_id] |= ptal
        return categories


class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    def _prepare_single_value_for_display(self):
        """On the product page group together the attribute lines that concern
        the same attribute and that have only one value each.

        Indeed those are considered informative values, they do not generate
        choice for the user, so they are displayed below the configurator.

        The returned attributes are ordered as they appear in `self`, so based
        on the order of the attribute lines.
        """
        single_value_lines = self.filtered(
            lambda ptal: len(ptal.value_ids) == 1)
        single_value_attributes = OrderedDict(
            [(pa, self.env['product.template.attribute.line']) for pa in single_value_lines.attribute_id])
        for ptal in single_value_lines:
            single_value_attributes[ptal.attribute_id] |= ptal
        return single_value_attributes
