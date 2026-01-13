import json


def load_default_products():
    with open("app/repositories/products.json", "r", encoding="utf-8") as file:
        default_products = json.load(file)
    return default_products
