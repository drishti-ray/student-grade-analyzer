students = []


# 1. Add Student
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")

    python = float(input("Enter Python marks: "))
    maths = float(input("Enter Mathematics marks: "))
    evs = float(input("Enter EVS marks: "))
    english = float(input("Enter English marks: "))

    student = {
        "id": student_id,
        "name": name,
        "python": python,
        "maths": maths,
        "evs": evs,
        "english": english
    }

    students.append(student)

    print("Student added successfully.")


# 2. Display Students
def display_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n===== STUDENT RECORDS =====")

    for student in students:
        print("\nStudent ID:", student["id"])
        print("Name:", student["name"])
        print("Python:", student["python"])
        print("Mathematics:", student["maths"])
        print("EVS:", student["evs"])
        print("English:", student["english"])


# 3. Calculate Result
def calculate_result():
    student_id = input("Enter student ID: ")

    for student in students:
        if student["id"] == student_id:

            total = (
                student["python"]
                + student["maths"]
                + student["evs"]
                + student["english"]
            )

            percentage = (total / 400) * 100

            if percentage >= 90:
                grade = "A+"
            elif percentage >= 80:
                grade = "A"
            elif percentage >= 70:
                grade = "B"
            elif percentage >= 60:
                grade = "C"
            elif percentage >= 50:
                grade = "D"
            else:
                grade = "F"

            print("\n===== STUDENT RESULT =====")
            print("Name:", student["name"])
            print("Total Marks:", total, "/ 400")
            print("Percentage:", percentage, "%")
            print("Grade:", grade)

            return

    print("Student not found.")


# 4. Find Top Student
def find_top_student():
    if len(students) == 0:
        print("No students found.")
        return

    top_student = students[0]

    for student in students:

        current_total = (
            student["python"]
            + student["maths"]
            + student["evs"]
            + student["english"]
        )

        top_total = (
            top_student["python"]
            + top_student["maths"]
            + top_student["evs"]
            + top_student["english"]
        )

        if current_total > top_total:
            top_student = student

    top_total = (
        top_student["python"]
        + top_student["maths"]
        + top_student["evs"]
        + top_student["english"]
    )

    print("\n===== TOP STUDENT =====")
    print("Student ID:", top_student["id"])
    print("Name:", top_student["name"])
    print("Total Marks:", top_total, "/ 400")


# 5. Calculate Class Average
def calculate_class_average():
    if len(students) == 0:
        print("No students found.")
        return

    total_marks = 0

    for student in students:

        total = (
            student["python"]
            + student["maths"]
            + student["evs"]
            + student["english"]
        )

        total_marks = total_marks + total

    average = total_marks / len(students)

    print("\n===== CLASS AVERAGE =====")
    print("Class Average:", round(average, 2), "out of 400")


# 6. Main Menu
while True:

    print("\n========================================")
    print("       STUDENT PERFORMANCE ANALYZER")
    print("========================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Calculate Result")
    print("4. Find Top Student")
    print("5. Calculate Class Average")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        display_students()

    elif choice == "3":
        calculate_result()

    elif choice == "4":
        find_top_student()

    elif choice == "5":
        calculate_class_average()

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice.")
