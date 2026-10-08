from inventory.find_resource import find_resource


def borrow_resource(
    resources,
    fellows,
    borrow_records,
    fellow_id,
    resource_id,
    quantity
):
    """
    Borrow a quantity of a resource for a fellow.

    Raises:
        ValueError: If the fellow/resource is invalid, quantity is invalid,
                    or insufficient stock is available.

    Returns:
        dict: The newly created borrowing record.
    """

    if fellow_id not in fellows:
        raise ValueError(f"Fellow ID '{fellow_id}' does not exist.")

    resource = find_resource(resources, resource_id)

    if resource is None:
        raise ValueError(f"Resource ID '{resource_id}' does not exist.")

    if isinstance(quantity, bool) or not isinstance(quantity, int):
        raise ValueError("Quantity must be an integer.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    if quantity > resource["available"]:
        raise ValueError(
            f"Insufficient stock. Only {resource['available']} "
            f"unit(s) of '{resource['name']}' are available."
        )

    # All validation has passed.
    record = {
        "fellow_id": fellow_id,
        "resource_id": resource_id,
        "quantity": quantity
    }

    resource["available"] -= quantity
    borrow_records.append(record)

    return record