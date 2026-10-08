def get_borrowed_quantity(borrow_records, fellow_id, resource_id):
    """
    Get the quantity of a resource currently borrowed by a fellow.

    Args:
        borrow_records (list): Current borrowing records.
        fellow_id (str): ID of the fellow.
        resource_id (str): ID of the resource.

    Returns:
        int: Total quantity currently borrowed.
    """
    total = 0

    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
        ):
            total += record["quantity"]

    return total