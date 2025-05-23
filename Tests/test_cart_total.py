import unittest
from ..shopping_cart import ShoppingCart


class TestCartTotal(unittest.TestCase):
    def setUp(self):
        self.cart = ShoppingCart()

    def test_empty_cart(self):
        self.assertEqual(self.cart.get_total(), 0)

    def test_total_calculation(self):
        self.cart.add_item("Хлеб", 40)
        self.cart.add_item("Сыр", 200)
        self.assertEqual(self.cart.get_total(), 240)
