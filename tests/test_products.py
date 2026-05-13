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

    assert len(category_info1.products) == 3
    assert len(category_info2.products) == 2

    assert category_info1.category_count == 2
    assert category_info2.category_count == 2

    assert category_info1.product_count == 5
    assert category_info2.product_count == 5
