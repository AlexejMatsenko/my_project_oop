def test_smartphone_init(smartphone_init):
    assert smartphone_init.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_init.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_init.price == 180000.0
    assert smartphone_init.quantity == 5
    assert smartphone_init.efficiency == 95.5
    assert smartphone_init.color == "Серый"
    assert smartphone_init.memory == 256
    assert smartphone_init.model == "S23 Ultra"
