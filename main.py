import csv

FILENAME = "student.csv"


# View All Students
def view_students():
    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            print("\n----- STUDENT RECORDS -----")

            for row in reader:
                print(row)

    except FileNotFoundError:
        print("File not found.")


# Add Student
def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course, marks])

    print("Student Added Successfully!")


# Search Student
def search_student():
    name = input("Enter Student Name: ")

    try:
        with open(FILENAME, "r") as file:
            reader = csv.reader(file)

            next(reader)      # Skip Header

            found = False

            for row in reader:
                if row[1].lower() == name.lower():
                    print("\nStudent Found")
                    print("------------------------")
                    print("ID :", row[0])
                    print("Name :", row[1])
                    print("Age :", row[2])
                    print("Course :", row[3])
                    print("Marks :", row[4])
                    found = True
                    break

            if not found:
                print("Student Not Found.")

    except FileNotFoundError:
        print("File not found.")



# Delete Student
def delete_student():
    student_id = input("Enter Student ID to Delete: ")

    rows = []
    found = False

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        for row in reader:
            if row[0] == "ID":      # Header
                rows.append(row)

            elif row[0] != student_id:
                rows.append(row)

            else:
                found = True

    with open(FILENAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    if found:
        print("Student Deleted Successfully!")
    else:
        print("Student Not Found.")


# Average Marks
def average_marks():
    total = 0
    count = 0

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        next(reader)  # Skip Header

        for row in reader:
            total += int(row[4])
            count += 1

    if count > 0:
        print("Average Marks :", total / count)
    else:
        print("No Student Records Found.")


# Highest Marks
def highest_marks():
    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        highest = None

        for row in reader:
            if highest is None or int(row[4]) > int(highest[4]):
                highest = row

    if highest:
        print("\n----- Highest Marks -----")
        print("ID :", highest[0])
        print("Name :", highest[1])
        print("Course :", highest[3])
        print("Marks :", highest[4])


# Total Students
def total_students():
    count = 0

    with open(FILENAME, "r") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            count += 1

    print("Total Students :", count)
# Main Menu
while True:

    print("1. View All Students")
    print("2. Add Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Average Marks")
    print("6. Highest Marks")
    print("7. Total Students")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        view_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()
    
    elif choice == "4":
        delete_student()

    elif choice == "5":
         average_marks()

    elif choice == "6":
         highest_marks()

    elif choice == "7":
         total_students()

    elif choice == "0":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")