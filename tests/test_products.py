import pytest
from src.products import Products

@pytest.fixture
def product_info():
    return Products("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_products(product_info):
    assert product_info.name == "Samsung Galaxy S23 Ultra"
    assert product_info.description == "256GB, Серый цвет, 200MP камера"
    assert product_info.price == 180000.0
    assert product_info.quantity == 5
