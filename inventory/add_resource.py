from inventory.find_resource import find_resource


def add_resource(resources, resource_id, name, category, total):
    """
    Add a new resource to the inventory.

    Args:
        resources (list): The current resource inventory.
        resource_id (str): Unique ID for the new resource.
        name (str): Name of the resource.
        category (str): Resource category.
        total (int): Total number of units.

    Returns:
        dict: The newly created resource.

    Raises:
        ValueError: If any validation fails.
    """

    if not isinstance(resource_id, str) or not resource_id.strip():
        raise ValueError("Resource ID cannot be empty.")

    if find_resource(resources, resource_id) is not None:
        raise ValueError(
            f"Resource ID '{resource_id}' already exists."
        )

    if not isinstance(name, str) or not name.strip():
        raise ValueError("Resource name cannot be empty.")

    if not isinstance(category, str) or not category.strip():
        raise ValueError("Resource category cannot be empty.")

    if isinstance(total, bool) or not isinstance(total, int):
        raise ValueError("Total units must be an integer.")

    if total <= 0:
        raise ValueError("Total units must be greater than zero.")

    resource = {
        "id": resource_id.strip(),
        "name": name.strip(),
        "category": category.strip(),
        "total": total,
        "available": total,
    }

    resources.append(resource)

    return resource