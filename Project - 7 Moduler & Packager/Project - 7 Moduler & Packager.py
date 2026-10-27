import datetime
import math
import random
import string
import time
import uuid
from toolkit.file_operations import create_file, write_file, read_file, append_file
from toolkit.math_utilities import convert_units, calculate_area

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        elif choice == "2":
            first = datetime.datetime.strptime(input("Enter first date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            second = datetime.datetime.strptime(input("Enter second date (YYYY-MM-DD): "), "%Y-%m-%d").date()
            print("Difference:", abs((second - first).days), "days")
        elif choice == "3":
            date_text = input("Enter date (YYYY-MM-DD): ")
            date_value = datetime.datetime.strptime(date_text, "%Y-%m-%d")
            print(date_value.strftime(input("Enter format (e.g. %d-%m-%Y): ")))
        elif choice == "4":
            input("Press Enter to start the stopwatch.")
            start = time.time()
            input("Press Enter to stop the stopwatch.")
            print("Elapsed time:", round(time.time() - start, 2), "seconds")
        elif choice == "5":
            seconds = int(input("Enter countdown seconds: "))
            while seconds > 0:
                print(seconds)
                time.sleep(1)
                seconds -= 1
            print("Time's up!")
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def math_menu():
    while True:
        print("\nMathematical Operations")
        print("1. Calculate factorial")
        print("2. Calculate compound interest")
        print("3. Trigonometric calculations")
        print("4. Area of geometric shapes")
        print("5. Unit conversion")
        print("6. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            number = int(input("Enter a non-negative integer: "))
            if number < 0:
                print("Number must be non-negative.")
            else:
                print("Factorial:", math.factorial(number))
        elif choice == "2":
            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter annual interest rate (%): "))
            years = float(input("Enter time in years: "))
            amount = principal * (1 + rate / 100) ** years
            print("Compound interest:", round(amount - principal, 2))
            print("Total amount:", round(amount, 2))
        elif choice == "3":
            degrees = float(input("Enter angle in degrees: "))
            radians = math.radians(degrees)
            print("sin:", round(math.sin(radians), 4))
            print("cos:", round(math.cos(radians), 4))
            print("tan:", round(math.tan(radians), 4))
            print("log:", math.log(float(input("Enter positive number for natural logarithm: "))))
        elif choice == "4":
            print("1. Circle  2. Rectangle  3. Triangle")
            shape = input("Choose shape: ")
            if shape == "1":
                print("Area:", round(calculate_area("circle", float(input("Enter radius: "))), 2))
            elif shape == "2":
                print("Area:", round(calculate_area("rectangle", float(input("Enter length: ")), float(input("Enter width: "))), 2))
            elif shape == "3":
                print("Area:", round(calculate_area("triangle", float(input("Enter base: ")), float(input("Enter height: "))), 2))
            else:
                print("Invalid shape.")
        elif choice == "5":
            value = float(input("Enter value: "))
            source = input("Convert from (km/m/cm): ").lower()
            target = input("Convert to (km/m/cm): ").lower()
            try:
                print("Converted value:", convert_units(value, source, target))
            except ValueError as error:
                print(error)
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def random_menu():
    while True:
        print("\nRandom Data Generation")
        print("1. Generate random number")
        print("2. Generate random list")
        print("3. Create random password")
        print("4. Generate random OTP")
        print("5. Random sampling")
        print("6. Game simulation")
        print("7. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("Random number:", random.randint(int(input("Minimum: ")), int(input("Maximum: "))))
        elif choice == "2":
            size = int(input("List size: "))
            low = int(input("Minimum value: "))
            high = int(input("Maximum value: "))
            print([random.randint(low, high) for _ in range(size)])
        elif choice == "3":
            length = int(input("Password length: "))
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
            password = ""
            for i in range(length):
                password += random.choice(characters)
            print("Generated password:", password)
        elif choice == "4":
            length = int(input("OTP length: "))
            otp = ""
            for i in range(length):
                otp += random.choice("0123456789")
            print("Generated OTP:", otp)
        elif choice == "5":
            values = input("Enter values separated by commas: ").split(",")
            count = int(input("Sample size: "))
            if 0 <= count <= len(values):
                print("Random sample:", random.sample(values, count))
            else:
                print("Sample size must be between zero and the number of values.")
        elif choice == "6":
            number = random.randint(1, 6)
            guess = int(input("Guess the dice number (1-6): "))
            print("Dice:", number)
            print("You win!" if guess == number else "Try again!")
        elif choice == "7":
            break
        else:
            print("Invalid choice.")

def uuid_menu():
    print("\nGenerate Unique Identifiers")
    print("UUID:", uuid.uuid4())

def file_menu():
    while True:
        print("\nFile Operations")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")
        choice = input("Enter your choice: ")
        filename = ""

        if choice in ("1", "2", "3", "4"):
            filename = input("Enter file name: ")
        if choice == "1":
            print(create_file(filename))
        elif choice == "2":
            print(write_file(filename, input("Enter data to write: ")))
        elif choice == "3":
            print(read_file(filename))
        elif choice == "4":
            print(append_file(filename, input("Enter data to append: ")))
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def explore_module():
    module_name = input("Enter module name to explore: ")
    modules = {
        "datetime": datetime,
        "math": math,
        "random": random,
        "time": time,
        "uuid": uuid,
        "toolkit.file_operations": __import__("toolkit.file_operations", fromlist=[""]),
        "toolkit.math_utilities": __import__("toolkit.math_utilities", fromlist=[""])
    }
    if module_name in modules:
        print("Available attributes:")
        print(dir(modules[module_name]))
    else:
        print("Module is not available in this toolkit.")

def main():
    while True:
        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()
        elif choice == "2":
            math_menu()
        elif choice == "3":
            random_menu()
        elif choice == "4":
            uuid_menu()
        elif choice == "5":
            file_menu()
        elif choice == "6":
            explore_module()
        elif choice == "7":
            print("Thank you for using the Multi-Utility Toolkit!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
