

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}/- ruppees")

class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def write_code(self):
        print(f"{self.name} The developer writes {self.language} code")

    def show_details(self):
        super().show_details()
        print(f"Language is {self.language}")
    def work(self):
        print(f"The developer {self.name} created webapp with {self.language}")

class Designer(Employee):
    def __init__(self, name, salary, tool):
        super().__init__(name, salary)
        self.tool = tool

    def design_page(self):
        print(f"{self.name} designed page using {self.tool}")

    def work(self):
        print(f"The designer {self.name} designed page with {self.tool}")

class Tester:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"The tester {self.name} testing the application")


developer1 = Developer("Arun", salary=5000, language="Python")
designer1 = Designer("Akhil", 3000, "Figma")
tester1 = Tester("Anila", 3500)

objects = [developer1, designer1, tester1]

for obj in objects:
    obj.work()
