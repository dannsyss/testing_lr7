class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            raise ValueError(f"Товар {item} уже есть в корзине")
        self.items[item] = price

    def remove_item(self, item):
        if item not in self.items:
            raise KeyError(f"Товар {item} отсутствует в корзине")
        del self.items[item]

    def get_total(self):
        return sum(self.items.values())
