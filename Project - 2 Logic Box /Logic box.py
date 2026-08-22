print("Welcome to the Pattern Generator and Number Analyzer!")

while True:
    print("\nSelect an option:")
    print("1. Generate a Pattern")
    print("2. Analyze a Range of Numbers")
    print("3. Exit")

    option = int(input("Enter your choice: "))

    if option == 1:
        while True:
            print("\nSelect the Pattern:")
            print("1. Right Triangle")
            print("2. Pyramid")
            print("3. Back to Main Menu")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    rows = int(input("Enter number of rows: "))

                    for i in range(1, rows + 1):
                        for j in range(i):
                            print("*", end=" ")
                        print()

                case 2:
                    rows = int(input("Enter number of rows: "))

                    for i in range(1, rows + 1):
                        spaces = rows - i
                        stars = 2 * i - 1
                        print(" " * spaces + "*" * stars)

                case 3:
                    print("Returning to main menu...")
                    break

                case _:
                    print("Invalid choice!")

    elif option == 2:
        start = int(input("\nEnter the start of the range: "))
        end = int(input("Enter the end of the range: "))

        if start > end:
            print("Invalid range! Start number should be smaller than end number.")

        else:
            total = 0
            print("\nNUMBER ANALYSIS")

            for number in range(start, end + 1):
                total += number

                if number % 2 == 0:
                    print(number, "is Even")
                else:
                    print(number, "is Odd")

            print("\nSum of numbers from", start, "to", end, "=", total)

    elif option == 3:
        print("\nThank you for using the program!")
        break

    else:
        print("\nInvalid choice! Please select between 1 and 3.")
