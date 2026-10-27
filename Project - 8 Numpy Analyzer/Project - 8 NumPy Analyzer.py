import numpy as np


class DataAnalytics:

    def __init__(self):
        self.array = None

    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            size = int(input("Enter the number of elements: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))

            if len(elements) == size:
                self.array = np.array(elements)
            else:
                print("Invalid number of elements.")
                return

        elif choice == 2:
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))

            if len(elements) == rows * columns:
                self.array = np.array(elements).reshape(rows, columns)
            else:
                print("Invalid number of elements.")
                return

        elif choice == 3:
            layers = int(input("Enter the number of layers: "))
            rows = int(input("Enter the number of rows: "))
            columns = int(input("Enter the number of columns: "))
            elements = list(map(int, input("Enter elements separated by space: ").split()))

            if len(elements) == layers * rows * columns:
                self.array = np.array(elements).reshape(layers, rows, columns)
            else:
                print("Invalid number of elements.")
                return

        else:
            print("Invalid choice.")
            return

        print("\nArray created successfully:")
        print(self.array)

    def indexing_slicing(self):
        if self.array is None:
            print("Create an array first.")
            return

        print("\nChoose an operation:")
        print("1. Indexing")
        print("2. Slicing")
        print("3. Go Back")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            index = int(input("Enter the index: "))
            try:
                print("Selected Element:", self.array.flat[index])
            except IndexError:
                print("Invalid index.")

        elif choice == 2:
            start = int(input("Enter the starting index: "))
            end = int(input("Enter the ending index: "))
            print("Sliced Array:")
            print(self.array.flat[start:end])

    def mathematical_operations(self):
        if self.array is None:
            print("Create an array first.")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")

        choice = int(input("Enter your choice: "))

        elements = list(map(float, input(
            "Enter the same number of elements separated by space: "
        ).split()))

        if len(elements) != self.array.size:
            print("Invalid number of elements.")
            return

        second_array = np.array(elements).reshape(self.array.shape)

        print("\nOriginal Array:")
        print(self.array)

        print("\nSecond Array:")
        print(second_array)

        if choice == 1:
            print("Result of Addition:")
            print(self.array + second_array)

        elif choice == 2:
            print("Result of Subtraction:")
            print(self.array - second_array)

        elif choice == 3:
            print("Result of Multiplication:")
            print(self.array * second_array)

        elif choice == 4:
            if np.any(second_array == 0):
                print("Division by zero is not allowed.")
            else:
                print("Result of Division:")
                print(self.array / second_array)

        elif choice == 5:
            print("Dot Product:")
            print(np.dot(self.array, second_array))

        elif choice == 6:
            if self.array.ndim == 2:
                print("Matrix Multiplication:")
                print(np.matmul(self.array, second_array))
            else:
                print("Matrix multiplication requires 2D arrays.")

    def combine_split_arrays(self):
        if self.array is None:
            print("Create an array first.")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            elements = list(map(int, input(
                "Enter elements for another array: "
            ).split()))

            if len(elements) != self.array.size:
                print("Invalid number of elements.")
                return

            second_array = np.array(elements).reshape(self.array.shape)

            print("Combined Array (Vertical Stack):")
            print(np.concatenate((self.array, second_array), axis=0))

        elif choice == 2:
            if self.array.size < 2:
                print("Array must contain at least two elements.")
                return

            parts = int(input("Enter the number of parts: "))

            try:
                print("Split Arrays:")
                print(np.array_split(self.array, parts))
            except ValueError:
                print("Invalid number of parts.")

    def search_sort_filter(self):
        if self.array is None:
            print("Create an array first.")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            value = float(input("Enter the value to search: "))
            positions = np.where(self.array == value)

            if len(positions[0]) > 0:
                print("Value found at positions:")
                print(positions)
            else:
                print("Value not found.")

        elif choice == 2:
            print("1. Ascending")
            print("2. Descending")

            order = int(input("Enter your choice: "))

            sorted_array = np.sort(self.array, axis=-1)

            if order == 2:
                sorted_array = np.flip(sorted_array, axis=-1)

            print("Sorted Array:")
            print(sorted_array)

        elif choice == 3:
            value = float(input("Enter the filter value: "))
            print("Values greater than the entered value:")
            print(self.array[self.array > value])

    def aggregates_statistics(self):
        if self.array is None:
            print("Create an array first.")
            return

        print("\nChoose a statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Sum:", np.sum(self.array))

        elif choice == 2:
            print("Mean:", np.mean(self.array))

        elif choice == 3:
            print("Median:", np.median(self.array))

        elif choice == 4:
            print("Standard Deviation:", np.std(self.array))

        elif choice == 5:
            print("Variance:", np.var(self.array))

        elif choice == 6:
            print("Minimum:", np.min(self.array))

        elif choice == 7:
            print("Maximum:", np.max(self.array))

        elif choice == 8:
            percentile = float(input("Enter percentile (0-100): "))

            if 0 <= percentile <= 100:
                print("Percentile:", np.percentile(self.array, percentile))
            else:
                print("Percentile must be between 0 and 100.")

        elif choice == 9:
            elements = list(map(float, input(
                "Enter the same number of elements for correlation: "
            ).split()))

            if len(elements) == self.array.size:
                second_array = np.array(elements).reshape(self.array.shape)

                print("Correlation Coefficient:")
                print(np.corrcoef(self.array.flatten(), second_array.flatten())[0, 1])
            else:
                print("Invalid number of elements.")


analytics = DataAnalytics()

while True:
    print("\nWelcome to the NumPy Analyzer!")
    print("1. Create a NumPy Array")
    print("2. Perform Mathematical Operations")
    print("3. Combine or Split Arrays")
    print("4. Search, Sort, or Filter Arrays")
    print("5. Compute Aggregates and Statistics")
    print("6. Indexing and Slicing")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        analytics.create_array()

    elif choice == "2":
        analytics.mathematical_operations()

    elif choice == "3":
        analytics.combine_split_arrays()

    elif choice == "4":
        analytics.search_sort_filter()

    elif choice == "5":
        analytics.aggregates_statistics()

    elif choice == "6":
        analytics.indexing_slicing()

    elif choice == "7":
        print("Thank you for using the NumPy Analyzer")
        break

    else:
        print("Invalid choice. Please try again.")