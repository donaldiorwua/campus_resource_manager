from demo.required_demo import run_required_demo


report = run_required_demo()

assert report["total_units"] == 18
assert report["available_units"] == 14
assert report["currently_borrowed"] == 4

low_stock_names = [
    resource["name"]
    for resource in report["low_stock_resources"]
]

assert low_stock_names == ["Keyboard"]

most_borrowed_names = [
    resource["name"]
    for resource in report["most_borrowed_resources"]
]

assert most_borrowed_names == ["Keyboard"]

print("\nAll required demonstration tests passed!")