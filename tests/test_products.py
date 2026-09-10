from unittest.mock import patch
from src.products import Product
import pytest


def test_product_info(product_info2):
    assert product_info2.name == "Samsung Galaxy S23 Ultra"
    assert product_info2.description == "Телефон б/у(10 лет)"
    assert product_info2.price == 1000
    assert product_info2.quantity == 1


def test_categories_info(category_info1, category_info2):
    assert category_info1.name == "Телефоны"
    assert category_info2.name == "Телевизоры"
    assert category_info1.description == "Телефоны разные, от новых до убитых"
    assert category_info2.description == "Новые"

    assert len(category_info1.products_in_list) == 3
    assert len(category_info2.products_in_list) == 2

    assert category_info1.category_count == 2
    assert category_info2.category_count == 2

    assert category_info1.product_count == 5
    assert category_info2.product_count == 5


def test_products_info_property(category_info2):
    assert category_info2.products == "Pazz, 20140 руб. Остаток: 4 шт.\nXiaomi, 27000 руб. Остаток: 6 шт.\n"


def test_products_price_setter(capsys, product_info2):
    product_info2.price = 0
    messedg = capsys.readouterr()
    assert messedg.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_add_product_count(category_info1, product_info2):
    category_info1.add_product(product_info2)
    assert len(category_info1.products_in_list) == 4


def test_new_product_dict(product_dict):
    assert product_dict.name == "Samsung Galaxy S23 Ultra"
    assert product_dict.description == "256GB, Серый цвет, 200MP камера"
    assert product_dict.price == 180000.0
    assert product_dict.quantity == 5


def test_str_category(category_info2):
    assert category_info2.__str__() == "\nТелевизоры, количество продуктов: 10 шт.\n"


def test_add_category(product_info2, product_info3):
    assert product_info2.__add__(product_info3) == 1681000.0


@patch("builtins.input", return_value="y")
def test_setter_price_yes(mocked_input, product_info2, price=100):
    if mocked_input:
        product_info2.price = product_info2.price - price
        assert product_info2.price == 900


def test_add_product_error(category_info2):
    with pytest.raises(TypeError):
        category_info2.add_product(1)


def test_add_product_priice_error(category_info2):
    with pytest.raises(TypeError):
        category_info2.__add__(1)


def test_quantity_error():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Iphone 15", "512GB, Gray space", 210000.0, 0)


def test_ZeroDivision_Error(category_info_arror):
    assert category_info_arror.middle_price() == 0


def test_middle_price(category_info2):
    assert category_info2.middle_price() == 23570.0
