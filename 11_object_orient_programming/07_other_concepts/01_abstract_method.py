"""
Learning: Abstract Method

An abstract method is a method that is declared
in a parent class but does not have a complete
implementation there.

Child classes must implement the abstract method.

In this example:

             Animal
                |
          +-----+-----+
          |           |
         Dog         Cat

Animal defines the abstract method:

    sound()

Dog and Cat must provide their own version of
sound().
"""


# ---------------------------------------------------
# Importing ABC Tools
# ---------------------------------------------------

from abc import ABC, abstractmethod


# ---------------------------------------------------
# Parent Class
# ---------------------------------------------------

# ABC means Abstract Base Class
class Animal(ABC):

    # Abstract Method
    @abstractmethod
    def sound(self):
        pass


# Dog inherits from Animal
class Dog(Animal):

    # Dog must implement sound()
    def sound(self):
        print("Dog says Woof")


# Cat inherits from Animal
class Cat(Animal):

    # Cat must implement sound()
    def sound(self):
        print("Cat says Meow")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

dog = Dog()
cat = Cat()


# ---------------------------------------------------
# Using Objects
# ---------------------------------------------------

dog.sound()
cat.sound()





"""
===================================================
DETAILED NOTE: ABSTRACT METHOD
===================================================

An abstract method is a method that is declared
in a parent class but does not have an actual
implementation.

It tells the child class:

    "You must create this method."


---------------------------------------------------
Example
---------------------------------------------------

In our example:

    class Animal(ABC):

        @abstractmethod
        def sound(self):
            pass


sound() is an abstract method.

Animal says:

    Every animal must have a sound() method.

But Animal does not define the actual sound.


---------------------------------------------------
Child Classes
---------------------------------------------------

Dog implements sound():

    def sound(self):
        print("Dog says Woof")


Cat implements sound():

    def sound(self):
        print("Cat says Meow")


So each child can have its own implementation.


---------------------------------------------------
Why use abstract methods?
---------------------------------------------------

They are useful when we want all child classes
to follow the same rule.

For example:

    Animal
      |
      +--- Dog   -> sound()
      |
      +--- Cat   -> sound()
      |
      +--- Cow   -> sound()


Every child must have sound().


---------------------------------------------------
Important
---------------------------------------------------

A class containing an abstract method cannot be
used to create a normal object.

So this is not allowed:

    animal = Animal()


Also, a child class must implement all abstract
methods before we can create its object.


---------------------------------------------------
Remember
---------------------------------------------------

Abstract method:

    Parent defines WHAT is required.

Child class defines:

    HOW it works.


In this example:

    Animal -> "Every animal must have sound()"

    Dog -> "Woof"

    Cat -> "Meow"


Simple definition:

    An abstract method is a method that forces
    child classes to provide their own implementation.
"""