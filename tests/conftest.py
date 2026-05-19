import pytest
from src.products import Product, Category


@pytest.fixture
def category_info1():
    return Category(
        name="Телефоны",
        description="Телефоны разные, от новых до убитых",
        products=[
            Product("Samsung Galaxy S23 Ultra", "Телефон новый,просто немножко упал(не работает камера)", 3999, 1),
            Product("Nokia", "б/у", 500, 2),
            Product(" Ulefone Power Armor 18T PRO", "Новый,прошёл все неоходимые тесты", "60000", 5),
        ],
    )


@pytest.fixture
def category_info2():
    return Category(
        name="Телевизоры",
        description="Новые",
        products=[
            Product("Pazz", "Телевизор 55 дюймов HC55USS26F UHD 4К Smart ОС Салют WiFi", 20140, 4),
            Product("Xiaomi", "Телевизор TV A 43 2025 черный", 27000, 6),
        ],
    )


@pytest.fixture
def product_info2():
    return Product("Samsung Galaxy S23 Ultra", "Телефон б/у(10 лет)", 1000, 1)


@pytest.fixture
def product_info3():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def object_json():
    return [
        {
            "name": "Смартфоны",
            "description": "Смартфоны, как средство не только коммуникации, "
            "но и получение дополнительных функций для удобства жизни",
            "products": [
                {
                    "name": "Samsung Galaxy C23 Ultra",
                    "description": "256GB, Серый цвет, 200MP камера",
                    "price": 180000.0,
                    "quantity": 5,
                }
            ],
        }
    ]


@pytest.fixture
def product_dict():
    return Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
