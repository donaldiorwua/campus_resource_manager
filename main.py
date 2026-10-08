from data.initial_data import resources, fellows

from cli.menu import show_menu
from cli.handlers import (
    handle_add_resource,
    handle_list_resources,
    handle_search_resources,
    handle_filter_resources,
    handle_borrow_resource,
    handle_return_resource,
    handle_inventory_report,
    handle_save_data,
    handle_load_data,
)


def main():
    borrow_records = []

    while True:
        choice = show_menu()

        if choice == "1":
            handle_add_resource(resources)

        elif choice == "2":
            handle_list_resources(resources)

        elif choice == "3":
            handle_search_resources(resources)

        elif choice == "4":
            handle_filter_resources(resources)

        elif choice == "5":
            handle_borrow_resource(
                resources,
                fellows,
                borrow_records,
            )

        elif choice == "6":
            handle_return_resource(
                resources,
                fellows,
                borrow_records,
            )

        elif choice == "7":
            handle_inventory_report(
                resources,
                borrow_records,
            )

        elif choice == "8":
            handle_save_data(
                resources,
                fellows,
                borrow_records,
                "campus_resource_data.json",
            )

        elif choice == "9":
            loaded_data = handle_load_data(
                "campus_resource_data.json"
            )

            if loaded_data is not None:
                (
                    loaded_resources,
                    loaded_fellows,
                    loaded_records,
                ) = loaded_data

                resources[:] = loaded_resources
                fellows.clear()
                fellows.update(loaded_fellows)
                borrow_records[:] = loaded_records

                print("Data loaded successfully.")

        elif choice == "0":
            print("Exiting Campus Resource Management System.")
            break


if __name__ == "__main__":
    main()