from src.products import Product


def test_mixin_product(capsys):
    Product("Samsung Galaxy S23 Ultra", "Телефон б/у(10 лет)", 1000, 1)
    message = capsys.readouterr()[0]
    assert message.strip() == "Product(Samsung Galaxy S23 Ultra, Телефон б/у(10 лет), 1000, 1)"
