
from datetime import timedelta

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.tools.misc import get_lang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare, float_round


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line.
        """
        for line in self:
            price = line.price_unit * (1 - (line.discount or 0.0) / 100.0)

            price_subtotal = price * line.product_uom_qty
            price_tax = price_subtotal * line.margin_percent * 0.06
            price_total = price_subtotal + price_tax
            # margin =  line.product_uom_qty * (price - line.purchase_price)

            if (price > 0):
                line.update({
                    'price_tax': price_tax,
                    'price_total': price_total,
                    'price_subtotal': price_subtotal,
                    # 'margin':margin
                })
            if self.env.context.get('import_file', False) and not self.env.user.user_has_groups('account.group_account_manager'):
                line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])