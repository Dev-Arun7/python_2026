"""
Class Method Example

This example demonstrates:
1. Instance attributes
2. Instance methods
3. Class attributes
4. Class methods
5. Using a class method to access class-level data

A class method belongs to the class rather than a specific object.
We use the @classmethod decorator to create a class method.

The first parameter of a class method is usually named `cls`.
`cls` refers to the class itself.
"""


class Student:
    # Class attributes
    # These values are shared by all Student objects
    student_count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        # Instance attributes
        # Each Student object gets its own name and gpa
        self.name = name
        self.gpa = gpa

        # Updating class attributes
        Student.student_count += 1
        Student.total_gpa += gpa

    # Instance method
    # Works with data belonging to a particular object, "self" is passed here.
    def get_info(self):
        print(f"{self.name} {self.gpa}")

    # Class method
    # Works with data belonging to the class, "cls" is passed here.
    @classmethod
    def get_student_count(cls):
        return f"Total num of students {cls.student_count}"

    # Class method
    # Calculates the average GPA using class-level data, instead of self, "cls" is passed
    @classmethod
    def avg_gpa(cls):
        if cls.student_count == 0:
            return 0
        else:
            return f"Average is {cls.total_gpa / cls.student_count}"


# Creating Student objects
student1 = Student(name="Arun", gpa=6.1)
student2 = Student("Anila", 8.6)
student3 = Student("Akhil", 9.3)


# Calling an instance method
# This method works with student1's data
student1.get_info()


# Accessing class attributes directly
print(Student.student_count)


# Calling a class method using the class
print(Student.avg_gpa())


"""
NOTE:

Instance method:
    - Uses `self`
    - Works with data belonging to a particular object
    - Example: student1.get_info()

Class method:
    - Uses `cls`
    - Uses data belonging to the class
    - Created using the @classmethod decorator
    - Can be called using the class
    - Example: Student.avg_gpa()

In this example:

    self  -> refers to a particular Student object
    cls   -> refers to the Student class

For example:

    student1.get_info()
    
Here, `self` refers to student1.

    Student.avg_gpa()

Here, `cls` refers to the Student class.

Class methods are useful when we want to work with
class-level data instead of data belonging to one specific object.
"""