import json


def load_data(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"Data file '{filename}' does not exist.")

    resources = data["resources"]
    fellows = data["fellows"]
    borrow_records = data["borrow_records"]

    return resources, fellows, borrow_records