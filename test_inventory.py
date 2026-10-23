import unittest
from product import Product
from inventory import Inventory

class TestInventory(unittest.TestCase):
    def test_add_and_total_value(self):
        inv = Inventory()
        inv.add(Product("Item1", "SKU001", 5.0, 2))
        inv.add(Product("Item2", "SKU002", 10.0, 1))
        self.assertEqual(inv.total_value(), 20.0)

    def test_low_stock(self):
        inv = Inventory()
        p1 = Product("Item1", "SKU001", 5.0, 2)
        p2 = Product("Item2", "SKU002", 10.0, 10)
        inv.add(p1)
        inv.add(p2)
        self.assertIn(p1, inv.low_stock())

if __name__ == "__main__":
    unittest.main()