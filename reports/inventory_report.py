def generate_inventory_report(resources, borrow_records):
    total_units = 0
    available_units = 0

    for resource in resources:
        total_units += resource["total"]
        available_units += resource["available"]

    currently_borrowed = total_units - available_units

    low_stock_resources = [
        resource
        for resource in resources
        if resource["available"] < 3
    ]

    borrowed_quantities = {}

    for resource in resources:
        borrowed_quantities[resource["id"]] = 0

    for record in borrow_records:
        resource_id = record["resource_id"]

        if resource_id in borrowed_quantities:
            borrowed_quantities[resource_id] += record["quantity"]

    most_borrowed_quantity = max(
        borrowed_quantities.values(),
        default=0
    )

    most_borrowed_resources = [
        resource
        for resource in resources
        if borrowed_quantities[resource["id"]] == most_borrowed_quantity
        and most_borrowed_quantity > 0
    ]

    return {
        "total_units": total_units,
        "available_units": available_units,
        "currently_borrowed": currently_borrowed,
        "low_stock_resources": low_stock_resources,
        "most_borrowed_resources": most_borrowed_resources,
    }