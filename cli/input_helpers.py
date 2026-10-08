def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.")


def get_integer_input(prompt):
    while True:
        value = input(prompt).strip()

        try:
            return int(value)
        except ValueError:
            print("Please enter a valid integer.")


def get_positive_integer_input(prompt):
    while True:
        value = input(prompt).strip()

        try:
            value = int(value)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if value <= 0:
            print("Value must be greater than zero.")
            continue

        return value