import json


def save_data(resources, fellows, borrow_records, filename):
    data = {
        "resources": resources,
        "fellows": fellows,
        "borrow_records": borrow_records,
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)