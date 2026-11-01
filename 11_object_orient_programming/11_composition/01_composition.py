
"""
Learning: Composition

Composition means:

    "One object contains another object."

In this example:

    A Car has an Engine.

The Engine is created separately and then
passed to the Car object.

        Car
         |
         | has
         ↓
       Engine

The important part is:

    self.engine = engine

A Car object can use the methods and variables
of its Engine object.
"""


# ---------------------------------------------------
# Engine Class
# ---------------------------------------------------

# Engine is a separate class
class Engine:

    # Constructor
    def __init__(self, manufacturer, horsepower):

        # Engine's own variables
        self.manufacturer = manufacturer
        self.horsepower = horsepower

    # Method to start the engine
    def start_engine(self):
        print(f"{self.manufacturer} engine started.")


# ---------------------------------------------------
# Car Class
# ---------------------------------------------------

class Car:

    # Constructor
    def __init__(self, brand, model, engine):

        # Car's own variables
        self.brand = brand
        self.model = model

        # Store the Engine object inside the Car object
        # The Car can now use the Engine's methods and variables
        self.engine = engine

    # Method to start the car
    def start_car(self):

        # Call the Engine object's method
        self.engine.start_engine()

        print(f"{self.brand} car started...")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Create an Engine object
engine1 = Engine("BMW", 150)

# Pass the Engine object to the Car constructor
# Now car1 contains engine1
car1 = Car("BMW", "X5", engine1)


# ---------------------------------------------------
# Composition
# ---------------------------------------------------

# Start the car
car1.start_car()


"""
===================================================
DETAILED NOTE: COMPOSITION
===================================================

What is Composition?
--------------------

Composition means:

    One object contains another object.

In simple words:

    One class uses an object created from another class.

For example:

    A Car has an Engine.

    A Computer has a Processor.

    A House has Rooms.

    A Library has Books.


---------------------------------------------------
Understanding Our Example
---------------------------------------------------

We have two separate classes:

    Engine
    Car

The Engine class handles engine-related operations.

The Car class handles car-related operations.

Instead of putting everything inside the Car class,
we create a separate Engine class.

This makes our code easier to organize and reuse.


---------------------------------------------------
Creating the Engine Object
---------------------------------------------------

Look at this:

    engine1 = Engine("BMW", 150)

We are creating an Engine object.

It contains:

    manufacturer = "BMW"
    horsepower = 150


---------------------------------------------------
Passing Engine to Car
---------------------------------------------------

Now look at this:

    car1 = Car("BMW", "X5", engine1)


We are passing the Engine object to the Car constructor.

Look at the Car constructor:

    def __init__(self, brand, model, engine):

It receives three values:

    brand
    model
    engine


The important part is:

    self.engine = engine


What does this mean?

    engine

    ↓

    The Engine object passed to the constructor.

    ↓

    self.engine

    ↓

    The Engine object is stored inside the Car object.


Now car1 has access to the Engine object.


---------------------------------------------------
Using the Engine Object Inside Car
---------------------------------------------------

Look at this method:

    def start_car(self):

        self.engine.start_engine()

        print(f"{self.brand} car started...")


Here:

    self.engine

refers to the Engine object stored inside the Car.

So:

    self.engine.start_engine()

means:

    Call the start_engine() method of the Engine object.


The Car does not need to know how the engine works.

It simply asks the Engine to start.


---------------------------------------------------
How Objects Are Connected
---------------------------------------------------

First:

    engine1 = Engine("BMW", 150)


We create an Engine object.


Next:

    car1 = Car("BMW", "X5", engine1)


We pass that Engine object to the Car.


The relationship looks like this:

    engine1
       |
       ↓
    Engine Object
       ↑
       |
    car1.engine
       ↑
       |
    Car Object


The Car object contains a reference to the Engine object.

Both refer to the same Engine object.


---------------------------------------------------
Why is Composition Useful?
---------------------------------------------------

Imagine we put all engine-related code directly
inside the Car class.

As the project grows, the Car class might become
very large.

Instead, we can separate responsibilities:

    Engine class
        - Engine manufacturer
        - Horsepower
        - Start engine

    Car class
        - Car brand
        - Car model
        - Start car


This makes the code:

    - Easier to organize.
    - Easier to maintain.
    - Easier to reuse.
    - Easier to understand.


---------------------------------------------------
Composition vs Inheritance
---------------------------------------------------

These are two different relationships.

Inheritance:

    IS A relationship

    A Dog IS AN Animal.

    class Dog(Animal):

Composition:

    HAS A relationship

    A Car HAS AN Engine.

    self.engine = engine


In inheritance, a child class gets features
from its parent class.

In composition, an object contains or uses
another object.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Composition means:

    Building a class using objects of other classes.

In this example:

    Car HAS AN Engine.


---------------------------------------------------
Main Idea
---------------------------------------------------

Instead of putting everything inside one class,
we can create separate classes for different tasks.

Then we can connect those objects together.

That is the main idea of Composition.
"""
