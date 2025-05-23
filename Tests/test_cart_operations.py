import unittest
from ..shopping_cart import ShoppingCart


class TestCartOperations(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_add_remove(self):
        self.cart.add_item("Яблоки", 50)
        self.assertIn("Яблоки", self.cart.items)

        self.cart.remove_item("Яблоки")
        self.assertNotIn("Яблоки", self.cart.items)

    def test_duplicate_item(self):
        self.cart.add_item("Молоко", 80)
        with self.assertRaises(ValueError):
            self.cart.add_item("Молоко", 80)
