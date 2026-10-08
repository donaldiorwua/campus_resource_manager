def show_menu():
    while True:
        print("\n=== Campus Resource Management System ===")
        print("1. Add resource")
        print("2. List resources")
        print("3. Search resources")
        print("4. Filter resources by category")
        print("5. Borrow resource")
        print("6. Return resource")
        print("7. View inventory report")
        print("8. Save data")
        print("9. Load data")
        print("0. Exit")

        choice = input("Enter your choice: ").strip()

        if choice in {
            "0",
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
        }:
            return choice

        print("Invalid choice. Please select a number from 0 to 9.")