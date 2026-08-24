

class Student:
    student_count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.student_count += 1
        Student.total_gpa += gpa

    # Instance method
    def get_info(self):
        print(f"{self.name} {self.gpa}")

    # Class method
    @classmethod
    def get_student_count(cls):
        return f"Total num of students {cls.student_count}"

    # Class method
    @classmethod
    def avg_gpa(cls):
        if cls.student_count == 0:
            return 0
        else:
            return f"Average is {cls.total_gpa / cls.student_count}"



student1 = Student(name="Arun", gpa=6.1)
student2 = Student("Anila", 8.6)
student3 = Student("Akhil", 9.3)

student1.get_info()



# Accessing class methods
print(Student.student_count)
print(Student.avg_gpa())