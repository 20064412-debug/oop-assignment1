# MiniMart Inventory (OOP Mini Project)

A small object-oriented inventory program: a `Product` class with validated
properties and factory tools, and an `Inventory` class that stores products
by SKU.

## Files
- `product.py` - the `Product` class
- `inventory.py` - the `Inventory` class
- `main.py` - demonstration script
- `test_product.py`, `test_inventory.py` - optional pytest tests (bonus)

## How to run
Requires Python 3.10+ and the standard library only.

    python main.py

Optional tests:

    pip install pytest
    pytest

## Design decisions
- **Encapsulation:** `price` and `quantity` are properties. `price` raises
  `TypeError` for non-numbers and `ValueError` for negatives; `quantity`
  accepts only non-negative integers. `line_value` and `is_low_stock` are
  read-only computed properties (low stock means quantity below 5).
- **No invalid Product can exist:** `__init__` assigns through the
  validating setters and also checks the SKU with `Product.is_valid_sku`.
- **Instance vs class data:** each object creates its own data in
  `__init__`. The only changing class attribute is the creation counter,
  read through `Product.count()`; failed products are not counted.
- **Factories:** `Product.from_csv_line` and `Inventory.from_lines` build
  objects from CSV text using `cls`.
- **Inventory:** a dict keyed by SKU gives fast lookup. A duplicate SKU
  raises `ValueError`; removing a missing SKU raises `KeyError`; `find`
  returns `None` when nothing matches.