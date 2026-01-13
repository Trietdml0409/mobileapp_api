import json



def accessJson():
    with open("default_products.json", "r", encoding="utf-8") as file:
        default_products = json.load(file)
    return default_products




