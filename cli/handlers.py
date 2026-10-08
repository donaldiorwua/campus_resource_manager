from inventory.add_resource import add_resource
from inventory.list_resources import list_resources
from inventory.search_resources import search_resources
from inventory.filter_resources import filter_by_category

from borrowing.borrow_resource import borrow_resource
from borrowing.return_resource import return_resource

from reports.inventory_report import generate_inventory_report

from persistence.save_data import save_data
from persistence.load_data import load_data

from cli.input_helpers import (
    get_non_empty_input,
    get_positive_integer_input,
)


def handle_add_resource(resources):
    resource_id = get_non_empty_input("Enter resource ID: ")
    name = get_non_empty_input("Enter resource name: ")
    category = get_non_empty_input("Enter resource category: ")
    total = get_positive_integer_input("Enter total units: ")

    try:
        resource = add_resource(
            resources,
            resource_id,
            name,
            category,
            total,
        )
    except ValueError as error:
        print(f"Error: {error}")
        return None

    print(
        f"Resource '{resource['name']}' "
        f"added successfully."
    )

    return resource


def handle_list_resources(resources):
    resources_list = list_resources(resources)

    if not resources_list:
        print("No resources found.")
        return resources_list

    for resource in resources_list:
        print(
            f"{resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Total: {resource['total']} | "
            f"Available: {resource['available']}"
        )

    return resources_list


def handle_search_resources(resources):
    search_term = get_non_empty_input("Enter search term: ")

    results = search_resources(resources, search_term)

    if not results:
        print("No matching resources found.")
        return results

    for resource in results:
        print(
            f"{resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Available: {resource['available']}"
        )

    return results


def handle_filter_resources(resources):
    category = get_non_empty_input("Enter category: ")

    results = filter_by_category(resources, category)

    if not results:
        print("No resources found in that category.")
        return results

    for resource in results:
        print(
            f"{resource['id']} | "
            f"{resource['name']} | "
            f"{resource['category']} | "
            f"Available: {resource['available']}"
        )

    return results


def handle_borrow_resource(
    resources,
    fellows,
    borrow_records,
):
    fellow_id = get_non_empty_input("Enter fellow ID: ")
    resource_id = get_non_empty_input("Enter resource ID: ")
    quantity = get_positive_integer_input("Enter quantity: ")

    try:
        record = borrow_resource(
            resources,
            fellows,
            borrow_records,
            fellow_id,
            resource_id,
            quantity,
        )
    except ValueError as error:
        print(f"Error: {error}")
        return None

    print(
        f"Successfully borrowed {record['quantity']} "
        f"unit(s) of resource '{record['resource_id']}'."
    )

    return record


def handle_return_resource(
    resources,
    fellows,
    borrow_records,
):
    fellow_id = get_non_empty_input("Enter fellow ID: ")
    resource_id = get_non_empty_input("Enter resource ID: ")
    quantity = get_positive_integer_input("Enter quantity: ")

    try:
        returned_quantity = return_resource(
            resources,
            fellows,
            borrow_records,
            fellow_id,
            resource_id,
            quantity,
        )
    except ValueError as error:
        print(f"Error: {error}")
        return None

    print(
        f"Successfully returned "
        f"{returned_quantity} unit(s) of resource "
        f"'{resource_id}'."
    )

    return returned_quantity


def handle_inventory_report(resources, borrow_records):
    report = generate_inventory_report(
        resources,
        borrow_records,
    )

    print(f"Total units: {report['total_units']}")
    print(f"Available units: {report['available_units']}")
    print(f"Currently borrowed: {report['currently_borrowed']}")

    print("\nLow stock resources:")

    if report["low_stock_resources"]:
        for resource in report["low_stock_resources"]:
            print(
                f"- {resource['name']}: "
                f"{resource['available']} available"
            )
    else:
        print("- None")

    print("\nMost borrowed resources:")

    if report["most_borrowed_resources"]:
        for resource in report["most_borrowed_resources"]:
            borrowed = (
                resource["total"] - resource["available"]
            )

            print(
                f"- {resource['name']}: "
                f"{borrowed} borrowed"
            )
    else:
        print("- None")

    return report


def handle_save_data(
    resources,
    fellows,
    borrow_records,
    filename,
):
    try:
        save_data(
            resources,
            fellows,
            borrow_records,
            filename,
        )
    except OSError as error:
        print(f"Error saving data: {error}")
        return False

    print("Data saved successfully.")
    return True


def handle_load_data(filename):
    try:
        return load_data(filename)
    except ValueError as error:
        print(f"Error: {error}")
        return None