def find_resource(resources, resource_id):
    """
    Find a resource by its unique ID.

    Args:
        resources (list): The current resource inventory.
        resource_id (str): The ID of the resource to find.

    Returns:
        dict: The matching resource if found.
        None: If no resource has the given ID.
    """

    for resource in resources:
        if resource["id"] == resource_id:
            return resource

    return None