from src.base_and_mixin_product import BaseProduct, ProductMixin

class Product(BaseProduct, ProductMixin):
    """Класс для представления продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float | int):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        elif price < self.__price:
            user_input = input("Согласны ли вы понизить текущую цену (у/no)?\n")
            if user_input == "no":
                return
            self.__price = price

    @classmethod
    def new_product(cls, product: dict):
        return cls(product["name"], product["description"], product["price"], product["quantity"])

    def __add__(self, other):
        if type(self) == type(other):
            return self.__price * self.quantity + other.__price * other.quantity

        raise TypeError


class Category(Product):
    """Класс для подсчета количества продуктов"""

    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None) -> None:
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    def __str__(self):
        count_quantity = 0
        for product in self.__products:
            count_quantity += product.quantity

        return f"\n{self.name}, количество продуктов: {count_quantity} шт.\n"

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        product_sum = ""
        for product in self.__products:
            product_sum += f"{str(product)}\n"
        return product_sum

    @property
    def products_in_list(self):
        return self.__products
