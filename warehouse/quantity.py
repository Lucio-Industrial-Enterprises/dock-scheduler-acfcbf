"""Parse pick-list quantities."""


def parse_quantity(value: str) -> int:
    """Return a nonnegative pick-list quantity."""
    quantity = int(value.strip())
    if quantity < 0:
        raise ValueError("quantity must not be negative")
    return quantity
