"""
Learning: Multiple Inheritance

Multiple inheritance means a child class can inherit
from more than one parent class.

        Father          Mother
           |               |
           |               |
           +-------+-------+
                   |
                 Child

Child inherits from both Father and Mother.
"""


# ---------------------------------------------------
# Father Class
# ---------------------------------------------------

class Father:

    # Method
    def drive(self):
        print("Father is driving.")


# ---------------------------------------------------
# Mother Class
# ---------------------------------------------------

class Mother:

    # Method
    def cook(self):
        print("Mother is cooking.")


# ---------------------------------------------------
# Child Class
# ---------------------------------------------------

# Child inherits from both Father and Mother
class Child(Father, Mother):

    # Child has its own method
    def play(self):
        print("Child is playing.")


# ---------------------------------------------------
# Creating Object
# ---------------------------------------------------

# Creating a Child object
child = Child()


# ---------------------------------------------------
# Using Child Object
# ---------------------------------------------------

# drive() comes from the Father class
child.drive()

# cook() comes from the Mother class
child.cook()

# play() comes from the Child class
child.play()





# ===================================================================================

"""
===================================================
DETAILED NOTE: MULTIPLE INHERITANCE
===================================================

What is Multiple Inheritance?
-----------------------------

Multiple inheritance means a class can inherit from
more than one parent class.

In this example:

        Father          Mother
           |               |
           |               |
           +-------+-------+
                   |
                 Child

The Child class inherits from both Father and Mother.

We wrote:

    class Child(Father, Mother):

This means:

    Child inherits from Father
    AND
    Child inherits from Mother


---------------------------------------------------
Why do we use Multiple Inheritance?
---------------------------------------------------

Sometimes a class needs features from more than
one class.

For example:

    Father
        -> drive()

    Mother
        -> cook()

    Child
        -> play()

A Child object can use all three methods because
Child inherits from both Father and Mother.

So we don't have to write drive() and cook() again
inside the Child class.


---------------------------------------------------
Understanding the Classes
---------------------------------------------------

Father class:

    class Father:

        def drive(self):
            print("Father is driving.")

The Father class has one method:

    drive()

This method belongs to the Father class.


Mother class:

    class Mother:

        def cook(self):
            print("Mother is cooking.")

The Mother class has one method:

    cook()

This method belongs to the Mother class.


Child class:

    class Child(Father, Mother):

        def play(self):
            print("Child is playing.")

The Child class has its own method:

    play()

But it also inherits:

    drive()    -> from Father
    cook()     -> from Mother


---------------------------------------------------
Creating the Object
---------------------------------------------------

We create a Child object:

    child = Child()

Now the object 'child' can access methods from:

    Father
    Mother
    Child

For example:

    child.drive()

Python finds drive() in the Father class.

    child.cook()

Python finds cook() in the Mother class.

    child.play()

Python finds play() in the Child class.


---------------------------------------------------
Important Point
---------------------------------------------------

Inheritance does not copy the methods into the
Child class.

Instead, the Child object can access methods from
its parent classes.

For example:

    child.drive()

Python looks for drive() in Child.

If it does not find it there, Python checks the
parent classes.

It finds drive() in Father.

Similarly:

    child.cook()

Python looks for cook() in Child.

It does not find it there, so it checks the parent
classes.

It finds cook() in Mother.


---------------------------------------------------
Single Inheritance vs Multiple Inheritance
---------------------------------------------------

Single inheritance:

    class Dog(Animal):

Here Dog has only one parent:

    Animal


Multiple inheritance:

    class Child(Father, Mother):

Here Child has two parents:

    Father
    Mother


So:

    One parent  -> Single inheritance

    Multiple parents -> Multiple inheritance


---------------------------------------------------
The Main Idea to Remember
---------------------------------------------------

Multiple inheritance means:

    One child class
            |
            +---- Parent 1
            |
            +---- Parent 2
            |
            +---- Parent 3
                    ...

A class can inherit from two or more classes.

In our example:

    Child(Father, Mother)

Child gets:

    drive() -> Father
    cook()  -> Mother
    play()  -> Child


---------------------------------------------------
What happens if both parents have the same method?
---------------------------------------------------

This is an important problem with multiple
inheritance.

For example, imagine both Father and Mother have:

    def speak(self):
        print("...")


Then Child gets 'speak()' from two different
parents.

Python needs to decide:

    Which speak() should be used?

Python solves this using something called:

    MRO

MRO means:

    Method Resolution Order

It defines the order in which Python searches
classes for a method.

We will learn MRO separately because it is an
important part of multiple inheritance.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Multiple inheritance:

    A child class inherits properties and methods
    from more than one parent class.


In this example:

    Child inherits from:

        Father
        Mother

Therefore:

    Child is an example of multiple inheritance.
"""