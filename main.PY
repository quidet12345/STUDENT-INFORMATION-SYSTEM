import os

def Courses():
    print("--------------------------COURSES--------------------------------")
    print("1. Bachelor of Science in Computer Technology")
    print("2. Bachelor of Science in Office Administration")
    print("3. Bachelor of Science in Business Administration")
    print("4. Bachelor of Criminology")
    print("5. Bachelor of Secondary Education")
    print("--------------------------COURSES--------------------------------")

def create_student():
    num_students = int(input("How many students would you like to register? "))
    with open("students.txt", "a") as file:
        for _ in range(num_students):
            print("\n-----Pill up form-----:")

            student_name = input("Enter the name of the student: ")
            student_birthday = input("Enter the birthday of the student (MM/DD/YYYY): ")
            student_origin = input("Enter the origin of the student (hometown, city, country): ")
            student_address = input("Enter the address of the student: ")

            file.write(f"{student_name}|{student_birthday}|{student_origin}|{student_address}\n")
    print(f"{num_students} student(s) have been registered successfully!")  

def read_students():
    if os.path.exists("students.txt"):
        with open("students.txt", "r") as file:
            students = file.readlines()
        if students:
            print("\nList of Registered Students:")
            for idx, student in enumerate(students, start=1):
                details = student.strip().split("|")
                print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Origin: {details[2]}, Address: {details[3]}")
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
                print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Origin: {details[2]}, Address: {details[3]}")

            try:
                student_idx = int(input("\nEnter the number of the student you want to update: ")) - 1
                if 0 <= student_idx < len(students):
                    new_name = input("Enter the new name for the student: ")
                    new_birthday = input("Enter the new birthday (MM/DD/YYYY): ")
                    new_origin = input("Enter the new origin: ")
                    new_address = input("Enter the new address: ")

                    students[student_idx] = f"{new_name}|{new_birthday}|{new_origin}|{new_address}\n"
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
                print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Origin: {details[2]}, Address: {details[3]}")

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
                    print(f"{idx}. Name: {details[0]}, Birthday: {details[1]}, Origin: {details[2]}, Address: {details[3]}")
            else:
                print(f"No students found with the name '{search_name}'.")
        else:
            print("No students are registered yet.")
    else:
        print("No student data file found.")

def menu():
    while True:
        print("\nSchool Management Database 2024")
        print("1. View Courses")
        print("2. Register Students")
        print("3. View Registered Students")
        print("4. Update Student Information")
        print("5. Delete Student")
        print("6. Search Student")
        print("7. Exit")

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
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

