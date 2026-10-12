class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):
    def __init__(self, *args):
        if len(args) == 2:
            name, age = args
            employee_id = None
            salary = None
        elif len(args) == 3:
            name, age, employee_id = args
            salary = None
        elif len(args) == 4:
            name, age, employee_id, salary = args
        else:
            raise TypeError("Invalid number of arguments")

        super().__init__(name, age)
        self.__employee_id = employee_id
        self.__salary = salary

    @property
    def employee_id(self):
        return self.__employee_id

    @employee_id.setter
    def employee_id(self, employee_id):
        self.__employee_id = employee_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

    def display(self):
        super().display()
        print("Employee ID:", self.__employee_id)
        print("Salary:", self.__salary)

    def __del__(self):
        if hasattr(self, "_Employee__employee_id"):
            del self._Employee__employee_id
        if hasattr(self, "_Employee__salary"):
            del self._Employee__salary


class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        super().display()
        print("Department:", self.department)


class Developer(Employee):
    def __init__(self, name, age, employee_id, salary, programming_language):
        super().__init__(name, age, employee_id, salary)
        self.programming_language = programming_language

    def display(self):
        super().display()
        print("Programming Language:", self.programming_language)


def create_person():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    return Person(name, age)


def create_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))

    print("\nChoose employee constructor:")
    print("1. Name and Age")
    print("2. Name, Age and Employee ID")
    print("3. Name, Age, Employee ID and Salary")

    choice = input("Enter your choice: ")

    if choice == "1":
        return Employee(name, age)

    elif choice == "2":
        employee_id = input("Enter Employee ID: ")
        return Employee(name, age, employee_id)

    elif choice == "3":
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        return Employee(name, age, employee_id, salary)

    else:
        print("Invalid choice.")
        return None


def create_manager():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")
    return Manager(name, age, employee_id, salary, department)


def create_developer():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    employee_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    programming_language = input("Enter Programming Language: ")
    return Developer(name, age, employee_id, salary, programming_language)


def show_details(records):
    if not records:
        print("No records available.")
        return

    print("\nChoose details to show:")
    print("1. Person")
    print("2. Employee")
    print("3. Manager")
    print("4. Developer")
    print("5. Check Inheritance")

    choice = input("Enter your choice: ")

    if choice == "1":
        for record in records:
            if type(record) is Person:
                print("\nPerson Details:")
                record.display()

    elif choice == "2":
        for record in records:
            if type(record) is Employee:
                print("\nEmployee Details:")
                record.display()

    elif choice == "3":
        for record in records:
            if isinstance(record, Manager):
                print("\nManager Details:")
                record.display()

    elif choice == "4":
        for record in records:
            if isinstance(record, Developer):
                print("\nDeveloper Details:")
                record.display()

    elif choice == "5":
        print("Manager is subclass of Employee:", issubclass(Manager, Employee))
        print("Developer is subclass of Employee:", issubclass(Developer, Employee))
        print("Employee is subclass of Person:", issubclass(Employee, Person))

    else:
        print("Invalid choice.")


def main():
    records = []

    while True:
        print("\n--- Python OOP Project: Employee Management System ---")
        print("\nChoose an operation:")
        print("1. Create a Person")
        print("2. Create an Employee")
        print("3. Create a Manager")
        print("4. Show Details")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            person = create_person()
            records.append(person)
            print("\nPerson created successfully.")
            person.display()

        elif choice == "2":
            employee = create_employee()

            if employee is not None:
                records.append(employee)
                print("\nEmployee created successfully.")
                employee.display()

        elif choice == "3":
            print("\nChoose employee type:")
            print("1. Manager")
            print("2. Developer")

            employee_type = input("Enter your choice: ")

            if employee_type == "1":
                manager = create_manager()
                records.append(manager)
                print("\nManager created successfully.")
                manager.display()

            elif employee_type == "2":
                developer = create_developer()
                records.append(developer)
                print("\nDeveloper created successfully.")
                developer.display()

            else:
                print("Invalid choice.")

        elif choice == "4":
            show_details(records)

        elif choice == "5":
            print("\nExiting the system.")
            records.clear()
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    main()
