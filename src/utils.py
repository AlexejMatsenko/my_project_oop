import json
import os
from src.products import Product, Category

def read_json(path):
    full_path = os.path.abspath(path)
    with open(full_path,"r", encoding="UTF-8") as file:
        data = json.load(file)
        return data


def write_json(data):
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
    result = write_json(json_file)
    print(result[0].name)
    print(result[0].products)


