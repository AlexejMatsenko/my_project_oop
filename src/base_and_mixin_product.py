from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Абстрактный класс"""

    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class ProductMixin:
    """Класс-миксин, который при создании объекта, выводит информацию о том,
    от какого класса и с какими параметрами был создан объект."""

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"
