import os

def Courses():
    print("--------------------------COURSES--------------------------------")
    print("1. Bachelor of Science in Information Technology")
    print("2. Bachelor of Science in Office Administration")
    print("3. Bachelor of Science in Business Administration")
    print("4. Bachelor of Criminology")
    print("5. Bachelor of Secondary Education")
    print("--------------------------COURSES--------------------------------")

def create_student():
    num_students = int(input("How many students would you like to register? "))
    with open("students.txt", "a") as file:
        for _ in range(num_students):
            print("\n-----Fill up form-----:")

            student_name = input("Enter the name of the student: ").capitalize()
            student_address = input("Enter the address of the student: ")
            
            while True:
                try:
                    student_birthday = input("Enter the birthday of the student (MM/DD/YYYY): ")
                    month, day, year = map(int, student_birthday.split("/"))
                
                    if (1900 <= year <= 3000) and (1<= month <= 12) and (1 <= day <= 31):
                        break
                    else:
                        print("Invalid date. Please enter a date in the format MM/DD/YYYY")
                except ValueError:
                    print("Invalid Input. Please enter only numbers.")
                          
            print("Select Course:")
                
            Courses()
            print("Select Course:")
            course_choice = input("Enter the number of the course: ")
            
            course_mapping = {
                '1': "Bachelor of Science in Information Technology",
                '2': "Bachelor of Science in Office Administration",
                '3': "Bachelor of Science in Business Administration",
                '4': "Bachelor of Criminology",
                '5': "Bachelor of Secondary Education"
            }
            student_course = course_mapping.get(course_choice, "Unknown Course")

            file.write(f"{student_name}|{student_birthday}|{student_address}|{student_course}\n")
    print(f"{num_students} student(s) have been registered successfully!")

def read_students():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()
        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start=1):
                details = student.strip().split("|")
                print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Address: {details[2]}, Course: {details[3]}")
        else:
            print("No students are registered yet.")
    else:
        print("No student data file found.")

def update_student():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()

        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start=1):
                details = student.strip().split("|")
                print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Address: {details[2]}, Course: {details[3]}")

            try:
                student_idx = int(input("\nEnter the number of the student you want to update: ")) - 1
                if 0 <= student_idx < len(students):
                    
                    new_name = input("Enter the new name for the student: ")
                    new_address = input("Enter the new address: ")
                    
                    while True:
                        try:
                            student_birthday = input("Enter the birthday of the student (MM/DD/YYYY): ")
                            month, day, year = map(int, student_birthday.split("/"))
                
                            if (1900 <= year <= 3000) and (1<= month <= 12) and (1 <= day <= 31):
                                break
                            else:
                                print("Invalid date. Please enter a date in the format MM/DD/YYYY")
                        except ValueError:
                            print("Invalid Input. Please enter only numbers.")
                   
                    Courses()
                    print("Select Course:")
                    course_choice = input("Enter the number of the course: ")
                    
                    course_mapping = {
                        '1': "Bachelor of Science in Information Technology",
                        '2': "Bachelor of Science in Office Administration",
                        '3': "Bachelor of Science in Business Administration",
                        '4': "Bachelor of Criminology",
                        '5': "Bachelor of Secondary Education"
                    }
                    student_course = course_mapping.get(course_choice, "Unknown Course")

                    students[student_idx] = f"{new_name}|{student_birthday}|{new_address}|{student_course}\n"
                    with open("students.txt", "w") as file:
                        file.writelines(students)
                    print("Student information has been updated.")
                else:
                    print("Invalid student number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No students to update.")
    else:
        print("No student data file found.")

def delete_student():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()

        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start=1):
                details = student.strip().split("|")
                print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Address: {details[2]}, Course: {details[3]}")

            try:
                student_idx = int(input("\nEnter the number of the student you want to delete: ")) - 1
                if 0 <= student_idx < len(students):
                    deleted_student = students.pop(student_idx)
                    with open("students.txt", "w") as file:
                        file.writelines(students)
                    print(f"Student '{deleted_student.strip().split('|')[0]}' has been deleted.")
                else:
                    print("Invalid student number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("No students to delete.")
    else:
        print("No student data file found.")

def search_student():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()

        if students:
            search_name = input("Enter the name of the student to search for: ").strip()
            found_students = [student.strip() for student in students if search_name.lower() in student.lower()]

            if found_students:
                print("\nSearch Results:")
                for idx, student in enumerate(found_students, start=1):
                    details = student.split("|")
                    print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Address: {details[2]}, Course: {details[3]}")
            else:
                print(f"No students found with the name '{search_name}'.")
        else:
            print("No students are registered yet.")
    else:
        print("No student data file found.")

def count_students_in_course():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()

        if students:
            print("Select Course to count students:")
            Courses()
            course_choice = input("Enter the number of the course: ")
            
            course_mapping = {
                '1': "Bachelor of Science in Information Technology",
                '2': "Bachelor of Science in Office Administration",
                '3': "Bachelor of Science in Business Administration",
                '4': "Bachelor of Criminology",
                '5': "Bachelor of Secondary Education"
            }
            selected_course = course_mapping.get(course_choice, "Unknown Course")
            
            
            count = sum(1 for student in students if selected_course in student)
            print(f"There are {count} students enrolled in the {selected_course}.")
        else:
            print("No students are registered yet.")
    else:
        print("No student data file found.")

def menu():
    while True:
        print("\nSTUDENT INFORMATION SYSTEM")
        print("1. View Courses")
        print("2. Register Students")
        print("3. View Registered Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Search Student")
        print("7. Count Students in Course")
        print("8. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            Courses()
        elif choice == '2':
            create_student()
        elif choice == '3':
            read_students()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            search_student()
        elif choice == '7':
            count_students_in_course()
        elif choice == '8':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

menu()