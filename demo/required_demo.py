from data.initial_data import resources, fellows

from inventory.search_resources import search_resources
from borrowing.borrow_resource import borrow_resource
from borrowing.return_resource import return_resource
from reports.inventory_report import generate_inventory_report


def run_required_demo():
    # Use fresh copies so the demonstration does not modify
    # the original initial data.
    demo_resources = [resource.copy() for resource in resources]
    demo_fellows = fellows.copy()
    demo_borrow_records = []

    print("=== Required Demonstration ===\n")

    # 1. F001 borrows 2 laptops
    borrow_resource(
        demo_resources,
        demo_fellows,
        demo_borrow_records,
        "F001",
        "R001",
        2,
    )

    print("1. F001 borrowed 2 laptops.")
    print("   Laptop available:", demo_resources[0]["available"])

    # 2. F002 borrows 3 keyboards
    borrow_resource(
        demo_resources,
        demo_fellows,
        demo_borrow_records,
        "F002",
        "R002",
        3,
    )

    print("2. F002 borrowed 3 keyboards.")
    print("   Keyboard available:", demo_resources[1]["available"])

    # 3. F001 returns 1 laptop
    return_resource(
        demo_resources,
        demo_fellows,
        demo_borrow_records,
        "F001",
        "R001",
        1,
    )

    print("3. F001 returned 1 laptop.")
    print("   Laptop available:", demo_resources[0]["available"])

    # 4. F003 requests 4 headsets
    headset_available_before = demo_resources[2]["available"]

    try:
        borrow_resource(
            demo_resources,
            demo_fellows,
            demo_borrow_records,
            "F003",
            "R003",
            4,
        )
    except ValueError as error:
        print("4. F003 requested 4 headsets.")
        print("   Rejected:", error)

    print(
        "   Headset stock unchanged:",
        demo_resources[2]["available"] == headset_available_before,
    )

    # 5. F002 returns 4 keyboards
    keyboard_available_before = demo_resources[1]["available"]

    try:
        return_resource(
            demo_resources,
            demo_fellows,
            demo_borrow_records,
            "F002",
            "R002",
            4,
        )
    except ValueError as error:
        print("5. F002 attempted to return 4 keyboards.")
        print("   Rejected:", error)

    print(
        "   Keyboard stock unchanged:",
        demo_resources[1]["available"] == keyboard_available_before,
    )

    # 6. Search for "LAPtop"
    search_results = search_resources(
        demo_resources,
        "LAPtop",
    )

    print("6. Search 'LAPtop':")

    for resource in search_results:
        print(
            f"   Found: {resource['id']} - "
            f"{resource['name']}"
        )

    # 7. Generate report
    report = generate_inventory_report(
        demo_resources,
        demo_borrow_records,
    )

    print("\n7. Final inventory report:")
    print("   Total units:", report["total_units"])
    print("   Available units:", report["available_units"])
    print(
        "   Currently borrowed:",
        report["currently_borrowed"],
    )

    print("   Low stock resources:")

    for resource in report["low_stock_resources"]:
        print(
            f"   - {resource['name']}: "
            f"{resource['available']} available"
        )

    print("   Most borrowed resources:")

    for resource in report["most_borrowed_resources"]:
        borrowed = resource["total"] - resource["available"]

        print(
            f"   - {resource['name']}: "
            f"{borrowed} borrowed"
        )

    return report


if __name__ == "__main__":
    run_required_demo()