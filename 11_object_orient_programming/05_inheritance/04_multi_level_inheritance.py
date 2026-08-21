"""
Learning: Multilevel Inheritance

Multilevel inheritance means a class inherits from
another class, and that class itself inherits from
another class.

Vehicle
   |
   ↓
  Car
   |
   ↓
SportsCar

Car inherits from Vehicle.

SportsCar inherits from Car.

Therefore, SportsCar can use methods from both
Car and Vehicle.
"""


# ---------------------------------------------------
# Vehicle Class
# ---------------------------------------------------

class Vehicle:

    # Method
    def start(self):
        print("Vehicle is starting.")

    # Method
    def stop(self):
        print("Vehicle is stopping.")


# ---------------------------------------------------
# Car Class
# ---------------------------------------------------

# Car inherits from Vehicle
class Car(Vehicle):

    # Method
    def drive(self):
        print("Car is driving.")


# ---------------------------------------------------
# SportsCar Class
# ---------------------------------------------------

# SportsCar inherits from Car
# Car itself inherits from Vehicle
class SportsCar(Car):

    # Method
    def speed(self):
        print("Sports car is going very fast.")


# ---------------------------------------------------
# Creating Object
# ---------------------------------------------------

# Creating a SportsCar object
sports_car = SportsCar()


# ---------------------------------------------------
# Using SportsCar Object
# ---------------------------------------------------

print("Sports Car:")

# start() comes from the Vehicle class
sports_car.start()

# drive() comes from the Car class
sports_car.drive()

# speed() comes from the SportsCar class
sports_car.speed()

# stop() comes from the Vehicle class
sports_car.stop()


"""
===================================================
DETAILED NOTE: MULTILEVEL INHERITANCE
===================================================

What is Multilevel Inheritance?
--------------------------------

Multilevel inheritance means inheritance happens
through multiple levels.

For example:

    Vehicle
       |
       ↓
      Car
       |
       ↓
    SportsCar


Here:

    Car inherits from Vehicle.

And:

    SportsCar inherits from Car.


Because SportsCar inherits from Car, and Car
inherits from Vehicle, SportsCar can also access
methods from Vehicle.

This creates a chain of inheritance.


---------------------------------------------------
Understanding the First Level
---------------------------------------------------

Vehicle is the parent class.

It has:

    start()
    stop()

These methods belong to Vehicle.


---------------------------------------------------
Understanding the Second Level
---------------------------------------------------

Car inherits from Vehicle:

    class Car(Vehicle):

Because of this, Car can use:

    start()
    stop()

Car also has its own method:

    drive()


So Car can use:

    start()  -> Vehicle
    stop()   -> Vehicle
    drive()  -> Car


---------------------------------------------------
Understanding the Third Level
---------------------------------------------------

SportsCar inherits from Car:

    class SportsCar(Car):

SportsCar gets the methods of Car.

But Car itself inherited methods from Vehicle.

Therefore SportsCar can access methods from
both levels above it.

SportsCar can use:

    start()  -> Vehicle
    stop()   -> Vehicle
    drive()  -> Car
    speed()  -> SportsCar


---------------------------------------------------
Why can SportsCar use start()?
---------------------------------------------------

We did not write:

    def start():

inside SportsCar.

So where does start() come from?

Python first looks inside SportsCar.

It does not find start().

Then Python looks at the parent class:

    Car

Car also does not have its own start() method.

So Python continues to Car's parent:

    Vehicle

Vehicle has start().

Therefore Python uses:

    Vehicle.start()


---------------------------------------------------
The Inheritance Chain
---------------------------------------------------

The complete chain is:

    Vehicle
       ↓
      Car
       ↓
    SportsCar


We can think about it like this:

    SportsCar
        ↓
       Car
        ↓
     Vehicle


So SportsCar can access methods available
through this inheritance chain.


---------------------------------------------------
Important Point
---------------------------------------------------

Multilevel inheritance is different from
multiple inheritance.

Multilevel inheritance:

    A
    ↓
    B
    ↓
    C


Multiple inheritance:

    A       B
     \     /
      \   /
        C


In multilevel inheritance, the inheritance is
a chain.

In multiple inheritance, one class has multiple
parents.


---------------------------------------------------
Example From This File
---------------------------------------------------

Multilevel inheritance:

    Vehicle
       ↓
      Car
       ↓
    SportsCar


Multiple inheritance would look like:

    Writer       Artist
        \         /
         \       /
        GraphicNovel


So remember:

    Multilevel = inheritance through levels

    Multiple = inheritance from multiple parents


---------------------------------------------------
What does SportsCar inherit?
---------------------------------------------------

SportsCar directly inherits from:

    Car

SportsCar does not directly write:

    class SportsCar(Vehicle):

But SportsCar can still access Vehicle methods
because Car inherited them from Vehicle.


This is one of the most important ideas in
multilevel inheritance.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Multilevel inheritance means:

    A class inherits from another class,
    which itself inherits from another class.

In our example:

    Car inherits from Vehicle.

    SportsCar inherits from Car.

Therefore:

    SportsCar can access methods from
    SportsCar, Car, and Vehicle.


---------------------------------------------------
Easy Way to Remember
---------------------------------------------------

Think of it as a family chain:

    Grandparent
        ↓
      Parent
        ↓
      Child


Similarly:

    Vehicle
        ↓
       Car
        ↓
    SportsCar


The lower class can get features from the
classes above it through inheritance.
"""