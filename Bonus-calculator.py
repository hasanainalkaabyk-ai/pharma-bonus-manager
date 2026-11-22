total_units = paid_units + bonus_units
raw_invoice_total = paid_units * unit_list_price
invoice_total = raw_invoice_total * (1 - extra_discount_percent / 100.0)

true_unit_cost = invoice_total / total_units
expected_profit_per_unit = selling_price_per_unit - true_unit_cost
total_expected_profit = expected_profit_per_unit * total_units

margin_percent = (
    (expected_profit_per_unit / selling_price_per_unit) * 100.0
    if selling_price_per_unit > 0
    else 0.0
)

return BonusDealResult(
    paid_units=paid_units,
    bonus_units=bonus_units,
    total_units=total_units,
    invoice_total=round(invoice_total, 2),
    true_unit_cost=round(true_unit_cost, 2),
    selling_price_per_unit=round(selling_price_per_unit, 2),
    expected_profit_per_unit=round(expected_profit_per_unit, 2),
    total_expected_profit=round(total_expected_profit, 2),
    margin_percent=round(margin_percent, 2),
)
