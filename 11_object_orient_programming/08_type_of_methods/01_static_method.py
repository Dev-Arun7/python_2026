"""
Learning: Static Method

A static method is a method that belongs to a class,
but it does not need the object (self) or the class (cls)
to do its work.

We use:

    @staticmethod

before the method.

In this example, we have a Student class.

The Student class has:

    info()
        -> Instance method
        -> Needs self
        -> Uses student data

    verify_age()
        -> Static method
        -> Does not need self
        -> Only works with the age given to it
"""

class Student:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    # Instance Method
    # It needs self because it uses the object's data.
    def info(self):
        print(f"{self.name} is studying {self.subject}")

    # Static Method
    # @staticmethod tells Python that this is a static method.
    #
    # This method does not need self.
    # It only needs the age value given to it.
    @staticmethod
    def verify_age(age):

        # Return True if age is 18 or above.
        # Otherwise return False.
        return True if age >= 18 else False


# ---------------------------------------------------
# Calling Static Method
# ---------------------------------------------------

# We can call a static method directly using the class. Not even creating an object

print(Student.verify_age(15))


# ---------------------------------------------------
# Creating Student Objects
# ---------------------------------------------------

student1 = Student("Arun", "Python")
student2 = Student("Anila", "Java")


# ---------------------------------------------------
# Calling Instance Method
# ---------------------------------------------------

# info() is an instance method.
# So we call it using the object.

student1.info()
student2.info()


"""
===================================================
DETAILED NOTE: STATIC METHOD
===================================================

What is a Static Method?
------------------------

A static method is a method that belongs to a class,
but it does not need:

    self
    or
    cls

to do its work.


We create a static method using:

    @staticmethod


---------------------------------------------------
Example
---------------------------------------------------

Inside our Student class:

    @staticmethod
    def verify_age(age):
        return True if age >= 18 else False


Here:

    verify_age()

does not need:

    self


It only needs:

    age


---------------------------------------------------
Why doesn't it need self?
---------------------------------------------------

Remember that self represents the current object.

For example:

    student1 = Student("Arun", "Python")


Here:

    student1.name
    student1.subject


are data belonging to student1.


Our info() method uses this data:

    def info(self):
        print(f"{self.name} is studying {self.subject}")


So info() needs self.


But verify_age() does not use:

    self.name
    self.subject


It only checks the age:

    age >= 18


Therefore, it does not need self.


---------------------------------------------------
Instance Method vs Static Method
---------------------------------------------------

Instance method:

    def info(self):


Static method:

    @staticmethod
    def verify_age(age):


The main difference is:

    Instance method
        ↓
    needs self
        ↓
    works with object data


    Static method
        ↓
    does not need self
        ↓
    works only with the values given to it


---------------------------------------------------
Calling the Static Method
---------------------------------------------------

We can call verify_age() directly using the class:

    Student.verify_age(15)


Here:

    Student
       ↓
    class

    verify_age()
       ↓
    static method

    15
       ↓
    age


The result is:

    False


Because:

    15 >= 18

is False.


For example:

    print(Student.verify_age(20))


Output:

    True


Because:

    20 >= 18

is True.


---------------------------------------------------
Why use a Static Method?
---------------------------------------------------

Sometimes we have a function that is logically related
to a class, but it does not need any object data.

In our example:

    verify_age()


is related to Student.

It makes sense to keep it inside the Student class.

But it does not need:

    self.name
    self.subject


So we make it a static method.


---------------------------------------------------
Instance Method Example
---------------------------------------------------

Our info() method is an instance method:

    def info(self):
        print(f"{self.name} is studying {self.subject}")


It needs self because it uses:

    self.name
    self.subject


When we do:

    student1.info()


Python uses the data from student1:

    student1.name
    student1.subject


So the output is:

    Arun is studying Python


---------------------------------------------------
Static Method Example
---------------------------------------------------

Our verify_age() method:

    @staticmethod
    def verify_age(age):
        return True if age >= 18 else False


It does not use:

    self.name
    self.subject


It only uses:

    age


Therefore, we can call it without creating a
Student object:

    Student.verify_age(20)


---------------------------------------------------
Important Point
---------------------------------------------------

A static method can be called using the class:

    Student.verify_age(20)


It can also be called using an object:

    student1.verify_age(20)


But the important point is:

    It does not receive self automatically.


The method only receives the value we pass:

    20


---------------------------------------------------
Simple Definition
---------------------------------------------------

A static method is:

    A method that belongs to a class but does not
    need the object's data or the class itself.


We use:

    @staticmethod


---------------------------------------------------
Main Idea
---------------------------------------------------

Ask yourself:

    "Does this method need information from the object?"


If YES:

    Use an instance method.

    def method(self):


If NO, but the method logically belongs to the class:

    A static method may be useful.

    @staticmethod
    def method(value):


In our example:

    info()
        ↓
    needs student information
        ↓
    instance method


    verify_age()
        ↓
    does not need student information
        ↓
    static method


That is the main idea of a static method.
"""