def normalize_discount(value):
    """Return a discount fraction."""
    return float(value)


def final_price(price, discount):
    return round(float(price) * (1.0 - normalize_discount(discount)), 2)
