from inventory.find_resource import find_resource
from borrowing.loan_helpers import get_borrowed_quantity


def return_resource(
    resources,
    fellows,
    borrow_records,
    fellow_id,
    resource_id,
    quantity
):
    """
    Return a quantity of a resource previously borrowed by a fellow.

    Raises:
        ValueError: If the fellow/resource is invalid, quantity is invalid,
                    or the fellow does not have enough units on loan.

    Returns:
        int: The quantity successfully returned.
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

    borrowed_quantity = get_borrowed_quantity(
        borrow_records,
        fellow_id,
        resource_id
    )

    if quantity > borrowed_quantity:
        raise ValueError(
            f"Cannot return {quantity} unit(s). "
            f"'{fellows[fellow_id]}' currently has only "
            f"{borrowed_quantity} unit(s) of '{resource['name']}' on loan."
        )

    remaining = quantity

    # Reduce existing borrowing records.
    for record in borrow_records:
        if (
            record["fellow_id"] == fellow_id
            and record["resource_id"] == resource_id
            and remaining > 0
        ):
            returned = min(record["quantity"], remaining)

            record["quantity"] -= returned
            remaining -= returned

    # Remove records whose quantity is now zero.
    borrow_records[:] = [
        record
        for record in borrow_records
        if record["quantity"] > 0
    ]

    resource["available"] += quantity

    return quantity