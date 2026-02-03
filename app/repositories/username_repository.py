import json


#Loading the product from json
def load_default_usernames():
    with open("app/repositories/usernames.json", "r", encoding="utf-8") as file:
        default_usernames = json.load(file)
    return default_usernames