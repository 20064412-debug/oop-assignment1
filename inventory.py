"""Inventory class for the MiniMart inventory program."""

from product import Product


class Inventory:
    """Stores products keyed by their SKU."""

    def __init__(self):
        self._products = {}  # per-instance dict: sku -> Product

    def __len__(self):
        return len(self._products)

    def __iter__(self):
        return iter(self._products.values())

    def add(self, product):
        """Add a product. Raises ValueError if the SKU already exists."""
        if not isinstance(product, Product):
            raise TypeError("add() expects a Product")
        if product.sku in self._products:
            raise ValueError(f"SKU {product.sku} is already in inventory")
        self._products[product.sku] = product

    def remove(self, sku):
        """Remove and return the product with this SKU (KeyError if missing)."""
        if sku not in self._products:
            raise KeyError(f"No product with SKU {sku}")
        return self._products.pop(sku)

    def find(self, sku):
        """Return the product with this SKU, or None if not found."""
        return self._products.get(sku)

    def total_value(self):
        """Total value of everything in stock."""
        return sum(product.line_value for product in self)

    def low_stock(self):
        """List of products that are running low."""
        return [product for product in self if product.is_low_stock]

    @classmethod
    def from_lines(cls, lines):
        """Build a complete inventory from a list of CSV lines."""
        inventory = cls()
        for line in lines:
            if line.strip():
                inventory.add(Product.from_csv_line(line))
        return inventory