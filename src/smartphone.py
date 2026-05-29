from src.products import Product


class Smartphone(Product):
    """Класс - наследник, который представляет категорию 'Смартфоны'"""

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        # Инициализация атрибутов категории
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
