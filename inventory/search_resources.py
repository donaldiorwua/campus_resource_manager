def search_resources(resources, search_term):
    """
    Search resources by name.

    The search is case-insensitive and supports partial matches.

    Args:
        resources (list): The current resource inventory.
        search_term (str): Text to search for in resource names.

    Returns:
        list: Resources whose names contain the search term.
    """

    search_term = search_term.strip().lower()

    return [
        resource
        for resource in resources
        if search_term in resource["name"].lower()
    ]