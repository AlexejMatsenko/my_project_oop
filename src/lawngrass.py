from src.products import Product


class LawnGrass(Product):
    """Класс - наследник, который представляет категорию 'Газонная трава'"""

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        # Инициализация атрибутов категории
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
