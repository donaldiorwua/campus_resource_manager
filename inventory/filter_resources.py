def filter_by_category(resources, category):
    """
    Filter resources by category.

    The comparison is case-insensitive.

    Args:
        resources (list): The current resource inventory.
        category (str): The category to filter by.

    Returns:
        list: Resources belonging to the given category.
    """
    category = category.strip().lower()

    return [
        resource
        for resource in resources
        if resource["category"].lower() == category
    ]