def input_data():
    """Input a 1D or 2D array from the user."""
    print("\nData Input Options:")
    print("1. 1D Array")
    print("2. 2D Array")
    choice = input("Enter choice: ")

    if choice == "1":
        n = int(input("\nEnter number of elements: "))
        data = []
        for i in range(n):
            value = int(input(f"Enter element {i + 1}: "))
            data.append(value)
        print("\nData stored successfully!")
        print("1D Array:", data)
        return data
    
    elif choice == "2":
        rows = int(input("\nEnter number of rows: "))
        columns = int(input("Enter number of columns: "))
        data = []
        for i in range(rows):
            row = []
            for j in range(columns):
                value = int(input(f"Enter value [{i + 1}][{j + 1}]:"))
                row.append(value)
            data.append(row)
        print("\nData stored successfully!")
        print("2D Array:")
        for row in data:
            print(row)
        return data

    else:
        print("\nInvalid choice.")
        return []


def display_data_summary(data):
    """Display dataset summary using built-in functions."""
    if len(data) == 0:
        print("\nDataset is empty. "
            "Please input data first.")
        return
    flat_data = []
    if isinstance(data[0], list):
        for row in data:
            for value in row:
                flat_data.append(value)

    else:
        flat_data = data.copy()
    total_elements = len(flat_data)
    minimum = min(flat_data)
    maximum = max(flat_data)
    total = sum(flat_data)
    average = total / total_elements
    print("\n" + "=" * 50)
    print("DATA SUMMARY")
    print("=" * 50)
    if isinstance(data[0], list):
        print("Array Type       : 2D Array")
    else:
        print("Array Type       : 1D Array")
    print("Total Elements   :", total_elements)
    print("Minimum Value    :", minimum)
    print("Maximum Value    :", maximum)
    print("Total Sum        :", total)
    print("Average          :", f"{average:.2f}")


def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def filter_data(data, threshold):
    """Filter dataset values using lambda and filter functions."""
    flat_data = []
    if isinstance(data[0], list):
        for row in data:
            for value in row:
                flat_data.append(value)

    else:
        flat_data = data.copy()
    filtered_data = list(filter(lambda value: value >= threshold, flat_data))
    return filtered_data


def sort_data(data, ascending=True):
    """Sort the dataset in ascending or descending order."""
    if len(data) == 0:
        print("\nDataset is empty. "
            "Please input data first.")
        return
    if isinstance(data[0], list):
        print("\nSorted 2D Array:")
        for row in data:
            sorted_row = sorted(row,reverse=not ascending)
            print(sorted_row)

    else:
        sorted_data = sorted(data,reverse=not ascending)
        print("\nSorted 1D Array:")
        print(sorted_data)


def get_dataset_statistics(*values):
    """Calculate and return multiple dataset statistics."""
    minimum = min(values)
    maximum = max(values)
    total = sum(values)
    average = total / len(values)
    return minimum, maximum, total, average


def display_dataset_statistics(data):
    """Display dataset statistics using multiple return values."""
    if len(data) == 0:
        print( "\nDataset is empty. "
            "Please input data first." )
        return
    flat_data = []
    if isinstance(data[0], list):
        for row in data:
            for value in row:
                flat_data.append(value)

    else:
        flat_data = data.copy()
    minimum, maximum, total, average = (get_dataset_statistics(*flat_data))
    print("\n" + "=" * 50)
    print("DATASET STATISTICS")
    print("=" * 50)
    print("Minimum Value :", minimum)
    print("Maximum Value :", maximum)
    print("Total Sum     :", total)
    print("Average Value :", f"{average:.2f}")


def show_doc():
    """Display documentation of the program functions."""
    print("\n" + "=" * 60)
    print("PROGRAM DOCUMENTATION")
    print("=" * 60)
    print("\nProject Documentation:")
    print(__doc__)
    print("\n1. input_data():")
    print(input_data.__doc__)
    print("\n2. display_data_summary():")
    print(display_data_summary.__doc__)
    print("\n3. factorial():")
    print(factorial.__doc__)
    print("\n4. filter_data():")
    print(filter_data.__doc__)
    print("\n5. sort_data():")
    print(sort_data.__doc__)
    print("\n6. get_dataset_statistics():")
    print(get_dataset_statistics.__doc__)
    print("\n7. display_dataset_statistics():")
    print(display_dataset_statistics.__doc__)
    print("\n8. main():")
    print(main.__doc__)


def main():
    """Run the Data Analyzer and Transformer Program."""
    data = []
    print("=" * 55)
    print("WELCOME TO THE DATA ANALYZER")
    print("AND TRANSFORMER PROGRAM")
    print("=" * 55)
    while True:
        print("\n" + "=" * 55)
        print("MAIN MENU")
        print("=" * 55)
        print("1. Input Data")
        print("2. Display Data Summary (Built-in Functions)")
        print("3. Calculate Factorial (Recursion)")
        print("4. Filter Data by Threshold (Lambda & Filter)")
        print("5. Sort Data")
        print("6. Display Dataset Statistics (Multiple Values)")
        print("7. Show __doc__")
        print("8. Exit")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            data = input_data()

        elif choice == "2":
            display_data_summary(data)

        elif choice == "3":
            num = int(input("\nEnter a number to calculate factorial: "))
            if num < 0:
                print("\nFactorial is not possible "
                    "for negative numbers.")

            else:
                result = factorial(num)
                print(f"\nFactorial of {num} is: {result}")

        elif choice == "4":
            if len(data) == 0:
                print("\nDataset is empty. "
                    "Please input data first.")
            else:
                threshold = int(input("\nEnter threshold value: "))
                filtered_data = filter_data(data, threshold)
                print( f"\nFiltered Data "
                    f"(values >= {threshold}):" )
                if len(filtered_data) == 0:
                    print("No values found.")
                else:
                    print(filtered_data)

        elif choice == "5":
            if len(data) == 0:
                print("\nDataset is empty. "
                    "Please input data first.")
            else:
                while True:
                    print("\nSort Data:")
                    print("1. Ascending")
                    print("2. Descending")
                    print("3. Exit")
                    sort_choice = input( "Enter your choice: ")
                    if sort_choice == "1":

                        sort_data(data, True )
                    elif sort_choice == "2":
                        sort_data(data, False)
                    elif sort_choice == "3":
                        break
                    else:
                        print("\nInvalid choice. "
                            "Please try again.")

        elif choice == "6":
            display_dataset_statistics(data)
            
        elif choice == "7":
            show_doc()

        elif choice == "8":
            print( "\nThank you for using the "
                "Data Analyzer and Transformer Program.")
            print("Goodbye!")
            break

        else:

            print("\nInvalid choice. "
                "Please try again.")


main()
