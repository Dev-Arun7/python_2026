"""
Learning: Duck Typing

Duck typing means:

    "If it behaves like the object we need,
     we can use it."

Python does not require objects to belong to
the same class.

In this example:

    Dog  -> speak()
    Cat  -> speak()
    Car  -> speak()

All three objects have a speak() method.

So we can call:

    animal.speak()

without checking whether the object is a Dog,
Cat, or Car.

The idea comes from:

    "If it walks like a duck and quacks like a duck,
     treat it like a duck."
"""



# Animal Class, Parent class
class Animal:

    def __init__(self):

        # Common variable for Animal objects
        self.alive = True


# Dog Class
class Dog(Animal):

    # Dog has a speak() method
    def speak(self):
        print("WOOF!")


# Cat Class
class Cat(Animal):

    # Cat has a speak() method
    def speak(self):
        print("MEOW!")


# Car Class
class Car:

    # Car is not an Animal.
    # But it also has a speak() method.
    def speak(self):
        print("HONK!")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# These objects belong to different classes.
animals = [
    Dog(),
    Cat(),
    Car()
]


# ---------------------------------------------------
# Duck Typing
# ---------------------------------------------------

# We do not check the object's class.
#
# We simply call speak().
#
# If the object has speak(), Python can call it.

for animal in animals:

    # Each object provides its own version of speak()
    animal.speak()


"""
===================================================
DETAILED NOTE: DUCK TYPING
===================================================

What is Duck Typing?
--------------------

Duck typing means Python cares about what an object
can do, rather than what class it belongs to.

In this example:

    Dog
    Cat
    Car

are different classes.

But all three have:

    speak()


So we can simply do:

    animal.speak()


---------------------------------------------------
What happens in the loop?
---------------------------------------------------

    for animal in animals:
        animal.speak()


When animal is a Dog:

    Dog.speak()
    -> WOOF!


When animal is a Cat:

    Cat.speak()
    -> MEOW!


When animal is a Car:

    Car.speak()
    -> HONK!


Python does not need to check:

    Is this a Dog?
    Is this a Cat?
    Is this a Car?


It only needs to know:

    Does this object have speak()?


---------------------------------------------------
Why is it called Duck Typing?
---------------------------------------------------

The common idea is:

    "If it walks like a duck and quacks like a duck,
     treat it like a duck."


In Python:

    If an object has the method we need,
    we can use that method.

---------------------------------------------------
Simple Definition
---------------------------------------------------

Duck typing means:

    We care about what an object can do,
    not what type of object it is.

In this example:

    Dog -> speak()
    Cat -> speak()
    Car -> speak()

All can be used with:

    animal.speak()
"""