"""
Learning: Inheritance

Inheritance means a child class can use
the variables and methods of a parent class.

Animal
   |
   |--- Dog
   |--- Cat
   |--- Mouse

Dog, Cat, and Mouse inherit from Animal.
"""


# ---------------------------------------------------
# Parent Class
# ---------------------------------------------------

class Animal:

    # Constructor
    def __init__(self, name):

        # Instance Variables
        self.name = name
        self.is_alive = True

    # Method
    def eat(self):
        print(f"{self.name} is eating.")

    # Method
    def sleep(self):
        print(f"{self.name} is sleeping.")


# ---------------------------------------------------
# Dog Class
# ---------------------------------------------------

# Dog inherits from Animal
class Dog(Animal):

    # Dog has its own speak() method
    def speak(self):
        print(f"{self.name} is barking.")
        print("BOW  WOOF  WOOF  WOOF")


# ---------------------------------------------------
# Cat Class
# ---------------------------------------------------

# Cat inherits from Animal
class Cat(Animal):

    # Cat has its own speak() method
    def speak(self):
        print(f"{self.name} is speaking.")
        print("Meow... meow... meow...")


# ---------------------------------------------------
# Mouse Class
# ---------------------------------------------------

# Mouse inherits from Animal
class Mouse(Animal):

    # Mouse has its own speak() method
    def speak(self):
        print(f"{self.name} is speaking.")
        print("Squeak... squeak... squeak...")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Creating a Dog object
dog = Dog("Killer")       # Yes, that dog from Tom & Jerry

# Creating a Cat object
cat = Cat("Tom")          # Why not Tom.....

# Creating a Mouse object
mouse = Mouse("Jerry")    # Obviously.


# ---------------------------------------------------
# Using Dog Object
# ---------------------------------------------------

print(f"Dog name is {dog.name}")

# eat() comes from the Animal class
dog.eat()

# speak() comes from the Dog class
dog.speak()

print()


# ---------------------------------------------------
# Using Cat Object
# ---------------------------------------------------

print(f"Cat name is {cat.name}")

# sleep() comes from the Animal class
cat.sleep()

# speak() comes from the Cat class
cat.speak()

print()


# ---------------------------------------------------
# Using Mouse Object
# ---------------------------------------------------

print(f"Mouse name is {mouse.name}")

# speak() comes from the Mouse class
mouse.speak()









# ===================================================
# BEGINNER NOTES
# ===================================================

"""
1. WHAT IS INHERITANCE?
---------------------------------------------------

Inheritance allows one class to use the variables
and methods of another class.

Here:

    Animal
       |
       |--- Dog
       |--- Cat
       |--- Mouse

Animal is the PARENT class.

Dog, Cat, and Mouse are CHILD classes.


2. WHY DO WE NEED INHERITANCE?
---------------------------------------------------

Imagine we DON'T use inheritance.

We would have to write the same code again
inside every class.

For example:

class Dog:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Cat:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


class Mouse:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


Notice that we are repeating the same code
again and again.

This is not a good approach.

If we have 10 different animal classes,
we may have to write the same code 10 times.


3. WITH INHERITANCE
---------------------------------------------------

Instead, we put the common code inside
the Animal class.

class Animal:

    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")


Then:

class Dog(Animal):
    ...


class Cat(Animal):
    ...


class Mouse(Animal):
    ...


Now Dog, Cat, and Mouse automatically get:

    name
    is_alive
    eat()
    sleep()


We only need to write the common code once.


4. CODE REUSABILITY
---------------------------------------------------

One of the biggest benefits of inheritance
is CODE REUSABILITY.

We write common code once in the parent class
and reuse it in many child classes.

For example:

Animal
    |
    |--- Dog
    |--- Cat
    |--- Mouse
    |--- Horse
    |--- Cow
    |--- Elephant

All of these animals can use:

    eat()
    sleep()

So we don't need to write these methods
inside every class.


5. EASY TO MODIFY
---------------------------------------------------

Another important benefit is that the code
becomes easier to modify.

Suppose we change the eat() method.

Instead of changing it in:

    Dog
    Cat
    Mouse
    Horse
    Cow
    Elephant

we can change it only in Animal.

For example:

class Animal:

    def eat(self):
        print(f"{self.name} is eating food.")


All child classes can use the updated method.

This saves time and reduces duplicate code.


6. LESS DUPLICATE CODE
---------------------------------------------------

Inheritance helps us avoid writing the same
code multiple times.

Without inheritance:

    Dog → eat()
    Cat → eat()
    Mouse → eat()

The same code is repeated.

With inheritance:

    Animal → eat()

    Dog → uses Animal's eat()
    Cat → uses Animal's eat()
    Mouse → uses Animal's eat()

So we write it only once.


7. CHILD CLASSES CAN HAVE THEIR OWN METHODS
---------------------------------------------------

Inheritance does NOT mean that every child
must be exactly the same.

A child class can have its own methods.

For example:

class Dog(Animal):

    def speak(self):
        print("Woof!")


class Cat(Animal):

    def speak(self):
        print("Meow!")


Dog and Cat both inherit from Animal.

But they can also have their own behavior.


8. METHOD OVERRIDING
---------------------------------------------------

A child class can create a method with the
same name as a method in the parent class.

This is called METHOD OVERRIDING.

For example:

class Animal:

    def speak(self):
        print("Animal is speaking.")


class Dog(Animal):

    def speak(self):
        print("Woof!")


Here both classes have:

    speak()


But Dog has its own version of speak().

So when we do:

dog.speak()

Python uses the Dog version.


9. PARENT CLASS = COMMON FEATURES
---------------------------------------------------

The parent class should normally contain
things that are common to all child classes.

In our example:

Animal has:

    name
    is_alive
    eat()
    sleep()

These are common to dogs, cats, and mice.


10. CHILD CLASS = SPECIAL FEATURES
---------------------------------------------------

Child classes can contain features that are
specific to that particular type.

For example:

Dog:

    speak()

Cat:

    speak()

Mouse:

    speak()

The child classes can also have completely
different methods if needed.


11. INHERITANCE SAVES TIME
---------------------------------------------------

Imagine a large project with:

    20 animal classes

If all animals need:

    name
    is_alive
    eat()
    sleep()

we don't need to write those things 20 times.

We can create them once in Animal
and let the other classes inherit them.


12. IMPORTANT IDEA
---------------------------------------------------

Think about inheritance like this:

PARENT:

    "I have some common features."

CHILD:

    "I will use those common features,
     but I can also have my own features."


For example:

Animal
    |
    |--- Dog

Animal gives Dog:

    name
    is_alive
    eat()
    sleep()

Dog adds:

    speak()


13. REAL-WORLD EXAMPLE
---------------------------------------------------

Think about a company.

There may be a common Employee class:

Employee
    |
    |--- Developer
    |--- Designer
    |--- Manager

Every employee may have:

    name
    salary
    employee_id

So these common things can be placed
inside Employee.

Developer can then have:

    write_code()

Designer can have:

    create_design()

Manager can have:

    manage_team()

This is the same idea as:

Animal
    |
    |--- Dog
    |--- Cat
    |--- Mouse


14. MAIN BENEFITS OF INHERITANCE
---------------------------------------------------

Inheritance provides several benefits:

    ✓ Code reuse
    ✓ Less duplicate code
    ✓ Easier maintenance
    ✓ Easier modification
    ✓ Cleaner code structure
    ✓ Common features can be kept in one place
    ✓ Child classes can have their own features
    ✓ Makes large projects easier to organize


15. SIMPLE WAY TO REMEMBER
---------------------------------------------------

Remember this:

    Parent class
        ↓
    Common things

    Child class
        ↓
    Special things


In our example:

    Animal
        ↓
    Common animal features

    Dog
        ↓
    Dog-specific features

    Cat
        ↓
    Cat-specific features

    Mouse
        ↓
    Mouse-specific features


So the main idea of inheritance is:

    "Write common code once,
     then reuse it in child classes."
"""