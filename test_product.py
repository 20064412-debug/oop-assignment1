import unittest
from product import Product

class TestProduct(unittest.TestCase):
    def test_product_creation(self):
        p = Product("Test", "TST001", 10.0, 5)
        self.assertEqual(p.name, "Test")
        self.assertEqual(p.sku, "TST001")
        self.assertEqual(p.price, 10.0)
        self.assertEqual(p.quantity, 5)

    def test_line_value(self):
        p = Product("Test", "TST001", 10.0, 5)
        self.assertEqual(p.line_value, 50.0)

if __name__ == "__main__":
    unittest.main()