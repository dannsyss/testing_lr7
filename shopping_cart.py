import unittest


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        # Добавляет товар в корзину с указанной ценой
        if item in self.items:
            raise ValueError(f"Товар {item} уже есть в корзине")
        self.items[item] = price

    def remove_item(self, item):
        # Удаляет товар из корзины
        if item not in self.items:
            raise KeyError(f"Товар {item} отсутствует в корзине")
        del self.items[item]

    def get_total(self):
        # Возвращает общую стоимость товаров в корзине
        return sum(self.items.values())


class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        # Настройка тестового окружения перед каждым тестом
        self.cart = ShoppingCart()
        self.test_items = [("Яблоки", 50), ("Молоко", 80), ("Хлеб", 40)]

    def test_add_item(self):
        # Тест добавления товаров в корзину
        for item, price in self.test_items:
            self.cart.add_item(item, price)
            self.assertIn(item, self.cart.items)
            self.assertEqual(self.cart.items[item], price)

        # Проверка на добавление дубликата
        with self.assertRaises(ValueError):
            self.cart.add_item("Яблоки", 50)

    def test_remove_item(self):
        # Тест удаления товаров из корзины
        for item, price in self.test_items:
            self.cart.add_item(item, price)

        # Удаляем один товар
        self.cart.remove_item("Молоко")
        self.assertNotIn("Молоко", self.cart.items)

        # Проверка на удаление несуществующего товара
        with self.assertRaises(KeyError):
            self.cart.remove_item("Сахар")

    def test_get_total(self):
        # Тест расчета общей стоимости
        # Проверка пустой корзины
        self.assertEqual(self.cart.get_total(), 0)

        # Добавляем товары и проверяем сумму
        total = 0
        for item, price in self.test_items:
            self.cart.add_item(item, price)
            total += price
            self.assertEqual(self.cart.get_total(), total)

        # Удаляем товар и проверяем сумму
        self.cart.remove_item("Хлеб")
        self.assertEqual(self.cart.get_total(), total - 40)

    def test_combined_operations(self):
        # Комплексный тест операций с корзиной
        self.cart.add_item("Чай", 100)
        self.assertEqual(self.cart.get_total(), 100)

        self.cart.add_item("Кофе", 200)
        self.assertEqual(self.cart.get_total(), 300)

        self.cart.remove_item("Чай")
        self.assertEqual(self.cart.get_total(), 200)

        self.cart.add_item("Печенье", 50)
        self.assertEqual(self.cart.get_total(), 250)


if __name__ == "__main__":
    unittest.main(verbosity=2)
