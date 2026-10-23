"""Product class for the MiniMart inventory program."""

import math
import re


class Product:
    """A product stocked by the store.

    Attributes:
        name: Display name of the product.
        sku: Stock-keeping code, e.g. "MLK001".
        price: Unit price (a non-negative number).
        quantity: Units on hand (a non-negative integer).
    """

    LOW_STOCK_THRESHOLD = 5
    _SKU_PATTERN = re.compile(r"[A-Z]{3}[0-9]{3}")
    _count = 0  # class attribute: how many Products were created

    def __init__(self, name, sku, price, quantity):
        if not Product.is_valid_sku(sku):
            raise ValueError(
                f"Invalid SKU {sku!r}: expected 3 capital letters "
                "followed by 3 digits (e.g. MLK001)"
            )
        self.name = name
        self.sku = sku
        self.price = price        # goes through the validating setter
        self.quantity = quantity  # goes through the validating setter
        Product._count += 1       # only valid products are counted

    def __repr__(self):
        return (
            f"Product({self.name!r}, {self.sku!r}, "
            f"{self._price!r}, {self._quantity!r})"
        )

    # ---------- Part 2: encapsulation & validation ----------
    @property
    def price(self):
        """Unit price; must be a non-negative number."""
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("price must be a number")
        if math.isnan(value) or value < 0:
            raise ValueError("price must not be negative")
        self._price = value

    @property
    def quantity(self):
        """Units on hand; must be a non-negative integer."""
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("quantity must be an integer")
        if value < 0:
            raise ValueError("quantity must not be negative")
        self._quantity = value

    @property
    def line_value(self):
        """Read-only: price multiplied by quantity."""
        return self._price * self._quantity

    @property
    def is_low_stock(self):
        """Read-only: True when quantity is below the threshold (5)."""
        return self._quantity < self.LOW_STOCK_THRESHOLD

    # ---------- Part 3: class tools & factories ----------
    @classmethod
    def from_csv_line(cls, line):
        """Build a Product from a line like "Milk,MLK001,1.25,12"."""
        parts = [part.strip() for part in line.split(",")]
        if len(parts) != 4:
            raise ValueError(
                f"Expected 'name,sku,price,quantity' but got {line!r}"
            )
        name, sku, price, quantity = parts
        return cls(name, sku, float(price), int(quantity))

    @staticmethod
    def is_valid_sku(sku):
        """True for codes of 3 capital letters followed by 3 digits."""
        return isinstance(sku, str) and bool(
            Product._SKU_PATTERN.fullmatch(sku)
        )

    @classmethod
    def count(cls):
        """Number of Product objects created so far."""
        return Product._count