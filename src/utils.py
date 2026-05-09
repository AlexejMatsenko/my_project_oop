import json
import os
from typing import Any

from src.products import Category, Product


def read_json(path: str) -> dict:
    """Функция чтения данных из json файла"""

    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def object_from_json(data: dict) -> list[Any]:
    """Функция для создания объекта классов"""

    list_product = []
    for date in data:
        list_products = []
        for product in date["products"]:
            list_products.append(Product(**product))
        date["products"] = list_products
        list_product.append(Category(**date))
    return list_product


if __name__ == "__main__":
    json_file = read_json("../data/products.json")
    result = object_from_json(json_file)
    print(result[0].name)
    print(result[0].products)
