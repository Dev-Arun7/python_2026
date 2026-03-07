"""
Learning: Class Variables vs Instance Variables

Instance Variable:
------------------
These belong to each object separately.
Each object can have different values.

Example:
student_1.name
student_2.name


Class Variable:
---------------
These belong to the class itself.
All objects share the same value.

Example:
Student.class_year
Student.num_students


In our previous Car example, things like:
model, year, color

were different for each object.
Those are instance variables.

But sometimes we want a value that is common
for every object. In that case we use
class variables.
"""


class Student:

    # ---------------------------------------------------
    # Class Variables

    class_year = 2024      # Same for all students
    num_students = 0       # Count how many student objects are created

    # ---------------------------------------------------
    # Constructor

    def __init__(self, name, age):

        # Instance Variables (different for each object)
        self.name = name
        self.age = age

        # Increment student count whenever a new object is created
        Student.num_students += 1


# ---------------------------------------------------
# Creating Student Objects

student_1 = Student("Arun", 12)
student_2 = Student("Anila", 14)
student_3 = Student("Akhil", 15)


# ---------------------------------------------------
# Accessing Instance Variables

print("Student 1 Name:", student_1.name)
print("Student 1 Age:", student_1.age)

print()


# ---------------------------------------------------
# Accessing Class Variables

# Best practice is accessing class variables
# using the class name rather than object name

print("Class Year:", Student.class_year)

print()


# ---------------------------------------------------
# Showing all students

students = [student_1, student_2, student_3]

print("Student List:")

for student in students:
    print(student.name, "-", student.age)

print()


# ---------------------------------------------------
# Total number of students

print(f"My graduating class of {Student.class_year} has {Student.num_students} students")