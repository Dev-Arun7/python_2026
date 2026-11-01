
"""
Learning: Advanced Composition

Composition means:

    One object contains other objects.

In our previous example:

    Car HAS an Engine.

Now we are taking it one step further.

    Car HAS an Engine.
    Car HAS a Fuel Tank.

        Car
       /   \
      /     \
     ↓       ↓
  Engine  Fuel Tank


Each class has its own responsibility.

Engine:
    Handles engine-related operations.

Fuel_Tank:
    Handles fuel-related operations.

Car:
    Uses both Engine and Fuel_Tank to perform
    car-related operations.


The important part is:

    self.engine = engine
    self.fuel_tank = fuel_tank

The Car object contains two different objects.
"""


# ---------------------------------------------------
# Engine Class
# ---------------------------------------------------

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
# Fuel Tank Class
# ---------------------------------------------------

class Fuel_Tank:

    # Constructor
    def __init__(self, capacity, fuel):

        # Fuel tank's own variables
        self.capacity = capacity
        self.fuel = fuel

    # Show the current fuel level
    def show_fuel(self):
        print(f"{self.fuel} Litre fuel is available")

    # Add fuel to the tank
    def refuel(self, amount):

        # Fuel amount must be greater than zero
        if amount <= 0:
            print("Invalid amount of fuel")
            return

        # Add the given amount of fuel
        self.fuel += amount

        # Fuel should not exceed the tank capacity
        if self.fuel > self.capacity:
            self.fuel = self.capacity

        print(f"Fuel Level: {self.fuel}")


# ---------------------------------------------------
# Car Class
# ---------------------------------------------------

class Car:

    # Constructor
    def __init__(self, brand, model, engine, fuel_tank):

        # Car's own variables
        self.brand = brand
        self.model = model

        # Store the Engine object inside the Car
        self.engine = engine

        # Store the Fuel_Tank object inside the Car
        self.fuel_tank = fuel_tank

    # Start the car
    def start_car(self):

        # Use the Engine object's method
        self.engine.start_engine()

        print(f"{self.brand} car started...!")

    # Drive the car
    def drive_car(self):

        # Check whether the tank has enough fuel
        # Driving requires 2 litres of fuel
        if self.fuel_tank.fuel < 2:

            print("Not enough fuel to drive...!")
            print(f"Remaining fuel: {self.fuel_tank.fuel}")

        else:

            # Reduce 2 litres from the Fuel_Tank object
            self.fuel_tank.fuel -= 2

            print(f"You drive {self.model} car :)")
            print(f"Remaining fuel: {self.fuel_tank.fuel}")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Creating two Engine objects
engine1 = Engine("BMW", 150)
engine2 = Engine("Toyota", 120)


# Creating two Fuel_Tank objects
fuel_tank1 = Fuel_Tank(20, 12)
fuel_tank2 = Fuel_Tank(25, 15)


# Creating two Car objects
# Each car receives its own Engine and Fuel_Tank objects

car1 = Car("BMW", "X5", engine1, fuel_tank1)
car2 = Car("Toyota", "Corolla", engine2, fuel_tank2)


# ---------------------------------------------------
# Using the Objects
# ---------------------------------------------------

# Start BMW
car1.start_car()

# Drive BMW
car1.drive_car()

# Check BMW's fuel
car1.fuel_tank.show_fuel()

print("-" * 40)

# Start Toyota
car2.start_car()

# Drive Toyota
car2.drive_car()

# Check Toyota's fuel
car2.fuel_tank.show_fuel()


"""
===================================================
DETAILED NOTE: ADVANCED COMPOSITION
===================================================

What are we learning?
---------------------

In the previous example, our Car class contained
one Engine object.

Now our Car class contains two different objects:

    Engine
    Fuel_Tank

This means one object can contain multiple objects.

    Car
     |
     |------ Engine
     |
     |------ Fuel_Tank


---------------------------------------------------
Understanding the Classes
---------------------------------------------------

We have three separate classes:

1. Engine

    Responsible for engine-related operations.

    - manufacturer
    - horsepower
    - start_engine()


2. Fuel_Tank

    Responsible for fuel-related operations.

    - capacity
    - fuel
    - show_fuel()
    - refuel()


3. Car

    Responsible for car-related operations.

    - brand
    - model
    - start_car()
    - drive_car()


Each class handles its own responsibility.


---------------------------------------------------
How Composition Works Here
---------------------------------------------------

Look at the Car constructor:

    def __init__(self, brand, model, engine, fuel_tank):

It receives four values:

    brand
    model
    engine
    fuel_tank


The important part:

    self.engine = engine
    self.fuel_tank = fuel_tank


What does this mean?

    engine

    ↓

    The Engine object passed to the constructor.

    ↓

    self.engine

    ↓

    The Engine object is stored inside the Car.


The same happens with Fuel_Tank.

    fuel_tank

    ↓

    The Fuel_Tank object passed to the constructor.

    ↓

    self.fuel_tank

    ↓

    The Fuel_Tank object is stored inside the Car.


Now the Car has access to both objects.


---------------------------------------------------
How Does the Car Use the Engine?
---------------------------------------------------

Look at:

    def start_car(self):

        self.engine.start_engine()

The Car uses the Engine object's method.

Here:

    self.engine

refers to the Engine object stored inside Car.

And:

    start_engine()

is the method belonging to the Engine class.

So:

    self.engine.start_engine()

means:

    Ask the Engine object to start the engine.


---------------------------------------------------
How Does the Car Use the Fuel Tank?
---------------------------------------------------

Look at:

    def drive_car(self):

        if self.fuel_tank.fuel < 2:

            print("Not enough fuel to drive...!")

        else:

            self.fuel_tank.fuel -= 2


Here:

    self.fuel_tank

refers to the Fuel_Tank object.

And:

    self.fuel_tank.fuel

accesses the fuel variable inside that object.

We can also modify it:

    self.fuel_tank.fuel -= 2

This reduces the fuel level by 2 litres.

The important thing is:

    We are directly accessing and modifying
    the Fuel_Tank object's variable.


---------------------------------------------------
Each Car Has Its Own Objects
---------------------------------------------------

Look at:

    engine1 = Engine("BMW", 150)
    engine2 = Engine("Toyota", 120)


We created two different Engine objects.


Next:

    fuel_tank1 = Fuel_Tank(20, 12)
    fuel_tank2 = Fuel_Tank(25, 15)


We created two different Fuel_Tank objects.


Finally:

    car1 = Car("BMW", "X5", engine1, fuel_tank1)

    car2 = Car("Toyota", "Corolla", engine2, fuel_tank2)


Now the relationship looks like this:


    car1 (BMW)
       |
       |------ engine1
       |
       |------ fuel_tank1


    car2 (Toyota)
       |
       |------ engine2
       |
       |------ fuel_tank2


Each car has its own Engine and Fuel_Tank objects.

If we drive car1, only fuel_tank1 loses fuel.

The fuel level of car2 remains unchanged.


---------------------------------------------------
Why Is This Useful?
---------------------------------------------------

Imagine building a real vehicle management system.

You might have:

    Car
     |
     |------ Engine
     |
     |------ Fuel Tank
     |
     |------ Battery
     |
     |------ GPS
     |
     |------ Music System


Instead of putting all the code inside one huge
Car class, we can create separate classes.

Each class handles its own operations.

The Car class simply connects and uses them.


---------------------------------------------------
Composition vs Inheritance
---------------------------------------------------

Inheritance:

    IS A relationship

    A Dog IS AN Animal.

    class Dog(Animal):


Composition:

    HAS A relationship

    A Car HAS AN Engine.

    self.engine = engine


Inheritance allows a child class to reuse
features from a parent class.

Composition allows one object to contain
and use other objects.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Advanced Composition means:

    One object contains multiple objects
    and uses them to perform its operations.


---------------------------------------------------
Main Idea
---------------------------------------------------

Instead of writing everything inside one class,
we can divide the responsibilities into
separate classes.

Then we connect those objects together.

The objects work together to perform a task.

That is the main idea of Composition.
"""
