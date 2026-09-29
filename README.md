# Student Grade Analyzer

## About the Project

I made this project using Python to keep track of student marks and check their performance.

The program allows the user to add student details, view the stored students, calculate a student's result, find the student with the highest marks, and calculate the class average.

I made it as a menu-driven program so that the user can choose what they want to do.

## What the Program Can Do

The program has the following options:

1. Add a student
2. Display all students
3. Calculate a student's result
4. Find the top student
5. Calculate the class average
6. Exit the program

## Student Details

For each student, the program stores:

* Student ID
* Name
* Python marks
* Mathematics marks
* EVS marks
* English marks

The marks are stored out of 100 for each subject, so the total is calculated out of 400.

## How the Result is Calculated

When I select the result option, the program asks for the student's ID.

It then calculates the total marks and percentage.

The percentage is calculated using:

```python
percentage = (total / 400) * 100
```

The grade is then assigned according to the percentage.

| Percentage   | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80 to 89     | A     |
| 70 to 79     | B     |
| 60 to 69     | C     |
| 50 to 59     | D     |
| Below 50     | F     |

## Finding the Top Student

The program compares the total marks of all the students that have been added.

The student with the highest total marks is displayed as the top student.

## Class Average

The class average is calculated using the total marks of all the students.

The average is displayed up to two decimal places.

## Python Concepts Used

While making this project, I used some basic Python concepts such as:

* Lists
* Dictionaries
* Functions
* `if`, `elif` and `else`
* `for` loops
* `while` loop
* User input
* Arithmetic calculations
* Menu-driven programming

## Data Structures

I used a **list** to store multiple student records.

```python
students = []
```

Each student is stored as a **dictionary**.

For example:

```python
student = {
    "id": student_id,
    "name": name,
    "python": python,
    "maths": maths,
    "evs": evs,
    "english": english
}
```

This makes it easier to store and access the different details of each student.

## Example

For example, if a student has the following marks:

```text
Python: 85
Mathematics: 90
EVS: 78
English: 88
```

The total marks are:

```text
341 / 400
```

The percentage is:

```text
85.25%
```

So the grade will be:

```text
A
```

## How to Run the Program
## How to Run the Program

### Requirements

* Python 3.x
* No external libraries are required.

### Steps

1. Clone the repository:
git clone https://github.com/drishti-ray/student-grade-analyzer.git
2. Open the project folder:
cd student-grade-analyzer
3. Run the program:
python studentproject.py
4. Follow the instructions shown in the terminal and enter the required student details.
The program runs completely through the command line and does not require a GUI or any additional software.


## Limitations

Currently, the student information is stored only while the program is running. If the program is closed, the records are lost.

The program also has four fixed subjects and does not currently have options to edit or delete a student.

## Future Improvements

Some things that could be added later are:

* Saving student records permanently using files or a database.
* Adding options to edit and delete students.
* Adding more subjects.
* Adding a graphical interface.
* Adding more detailed student performance reports.

## Conclusion

This project helped me understand how different Python concepts can be combined to make a simple useful program.

I used lists, dictionaries, functions, loops and conditional statements to create a basic system for analyzing student performance.
