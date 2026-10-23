"""Demonstration script for the MiniMart inventory program."""

from inventory import Inventory
from product import Product

SAMPLE = [
    "Milk,MLK001,1.25,12",
    "Bread,BRD002,0.90,3",
    "Eggs,EGG003,2.40,30",
    "Coffee,COF004,7.50,2",
]


def print_report(inventory):
    """Print each product with its line value, the total and low stock."""
    print("MiniMart Inventory Report")
    print("=" * 52)
    print(f"{'Name':<10}{'SKU':<10}{'Price':>8}{'Qty':>6}{'Value':>12}")
    print("-" * 52)
    for product in inventory:
        print(
            f"{product.name:<10}{product.sku:<10}"
            f"{product.price:>8.2f}{product.quantity:>6}"
            f"{product.line_value:>12.2f}"
        )
    print("-" * 52)
    print(f"Total inventory value: {inventory.total_value():.2f}")
    print("Low-stock items:")
    for product in inventory.low_stock():
        print(f"  - {product.name} ({product.sku}): {product.quantity} left")
    print(f"Products created: {Product.count()}")


def main():
    inventory = Inventory.from_lines(SAMPLE)
    print_report(inventory)

main()