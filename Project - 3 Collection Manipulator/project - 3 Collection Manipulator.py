students=[]

while True:
    print("-------------------------------------------")
    print("Welcome to the Student Data Organizer!")
    print("-------------------------------------------")
    print()
    print("\nSelact an option:")
    print("1. Add Student")
    print("2. Disply All Student")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")

    chioce = int(input("Enter your choice::"))

    match chioce:
        case 1:
            print("---------------------------")
            student_id = int(input("student ID:"))
            name = input("Name :")
            age = int(input("Age :"))
            grade = input("Grade :")
            dob = input("Date of Birth (YYYY-MM-DD) :")
            email = input("Email :")
            phone = input("Phone number :")
            city = input("City name :")

            subject_input = input("Subjects (Comma-separated) :")
            subjects = set(subject_input.split(","))

            student = {
                "id":student_id,
                "name":name,
                "age":age,
                "dob":dob,
                "email":email,
                "phone":phone,
                "grade":grade,
                "city":city,
                "subjects":subjects
                }
            students.append(student)
            print("Student added successfully!")
            print("------------------------------")
                      
        case 2:
            
            print("\n----- All Students -----")

            if len(students) == 0:
                print("No student found.")
                      
            else:
                for student in students:
                    print("\n------*------*------*------")
                    print(f"Student ID:: {student['id']}")
                    print(f"Name :: {student['name']}")
                    print(f"Age :: {student['age']}")
                    print(f"Grade :: {student['grade']}")
                    print(f"Date of Birth :: {student['dob']}")
                    print(f"Subject :: {student['subjects']}")
                    print(f"Email :: {student['email']}")
                    print(f"Phone :: {student['phone']}")
                    print(f"City :: {student['city']}")
                    print("------*------*------*------")
                
        case 3:

            print("*-----*-----*-----*-----*")
            print("\n---- Update Student ----")
            student_id = int(input("Enter Student ID to update :"))
            found = False
            for student in students:
                if student["id"] == student_id:
                    print("\nStudent Found!")
                    new_name = input("Enter New Name :")
                    new_age = input("Enter New Age :")
                    new_email = input("Enter New Email :")
                    new_phone = input("Enter New Phone :")
                    new_grade = input("Enter New Grade :")
                    new_city = input("Enter New City :")

                    student["name"] = new_name
                    student["age"] = new_age
                    student["email"] = new_email
                    student["phone"] = new_phone
                    student["grade"] = new_grade
                    student["city"] = new_city
                    
                    print("\nstudent updated successfully!")
                    
                    found = True
                    break
                
                if found == False:
                    
                    print("Student not found.")
            print("*-----*-----*-----*-----*")   
                    
        case 4:
            print("===========================")
            
            print("\n--- Delete Student ---")

            student_id = int(input("Enter Student ID to delete: "))

            found = False

            for i in range(len(students)):

                if students[i]["id"] == student_id:

                    students.pop(i)

                    print("Student deleted successfully!")

                    found = True
                    break

            if found == False:
                print("Student not found.")
            print("============================")
        
        case 5:
        
            print("\n--- All Subjects Offered ---")

            all_subjects = set()

            for student in students:

                all_subjects.update(
                    student["subjects"]
                )

            if len(all_subjects) == 0:

                print("No subjects found.")

            else:

                for subject in all_subjects:

                    print(subject.strip())
                    

        case 6:
            print("**---**---**---**---**---**---**---**")
            print("Thank you for using the Student Data Organizer!")
            print("**---**---**---**---**---**---**---**")
            break
        case _:
            print("Invalid choice!")





    
