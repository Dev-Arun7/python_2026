import random




# ==========================================================
# Car Class
# ----------------------------------------------------------
# Represents a single car.
#
# The Car object stores:
# - Car information (name, fuel, speed)
# - Current driver
#
# The Car knows how to:
# - Start
# - Stop
# - Accelerate
# - Brake
# - Show its status
# This example python code shows how use class
# ==========================================================
class Car:

    def __init__(self, car_name, driver):
        # Basic information
        self.car_name = car_name
        self.fuel = 20
        self.speed = 0
        self.engine = False

        # Store the Driver object.
        # We keep the whole object instead of copying
        # values like driver.name or driver.acceleration.
        self.driver = driver

    # Called automatically when print(car) is used.
    def __str__(self):
        return f"{self.car_name} | speed={self.speed}"

    # Turn on the engine.
    def start(self):
        self.engine = True
        print(f"{self.driver.name} started {self.car_name}")

    # Turn off the engine.
    def stop(self):
        self.engine = False
        print(f"{self.driver.name} stopped {self.car_name}")

    # Increase the speed.
    #
    # The driver's acceleration skill affects
    # how much the speed increases.
    def accelerate(self):
        print("Accelerating....")
        self.speed += random.randint(1, self.driver.acceleration)
        print("Speed:", self.speed)

    # Reduce the speed.
    def breake_car(self):
        print("Breaking.....")
        self.speed -= random.randint(1, 10)
        print(f"Speed is: {self.speed}")

    # Print all information about this car.
    def status(self):
        print(f"---------{self.car_name}----------")
        print(f"Engine : {self.engine}")
        print(f"Speed  : {self.speed}")
        print(f"Fuel   : {self.fuel}")
        print(f"Driver : {self.driver.name}")
        print("--------------------------")


# ==========================================================
# Driver Class
# ----------------------------------------------------------
# Represents one driver.
#
# Every driver has different abilities.
# Later we can add:
# - experience
# - age
# - reaction_time
# - driving_skill
# ==========================================================
class Driver:

    def __init__(self, name):
        self.name = name
        self.top_speed = random.randint(100, 200)
        self.acceleration = random.randint(5, 20)
        self.height = random.randint(150, 190)


# ==========================================================
# Helper Functions
# ----------------------------------------------------------
# These are not part of the Car class.
# They coordinate objects.
# ==========================================================

# Perform a driving routine.
def drive(car):
    car.start()
    car.accelerate()
    car.accelerate()
    car.breake_car()
    car.accelerate()
    car.status()


# Perform a parking routine.
def park(car):
    car.breake_car()
    car.stop()
    car.status()


# Compare two cars and return the winner.
def race(car1, car2):

    if car1.speed > car2.speed:
        return car1.car_name

    elif car2.speed > car1.speed:
        return car2.car_name

    return "Draw"


# ==========================================================
# Main Function
# ----------------------------------------------------------
# Create all objects.
# Connect them together.
# Run the program.
# ==========================================================
def main():

    driver1 = Driver("Arun")
    driver2 = Driver("Akhil")

    car1 = Car("BMW", driver1)
    car2 = Car("AUDI", driver2)

    drive(car1)
    drive(car2)

    winner = race(car1, car2)

    print(f"\nWinner: {winner}")


# Program starts here.
if __name__ == "__main__":
    main()





"""
============================================================
                OOP LEARNING NOTES
============================================================

Project:
--------
Simple Car and Driver Simulation

Purpose:
--------
This project was created to understand the basics of
Object-Oriented Programming (OOP) in Python.

Instead of only learning syntax, the goal is to understand
how classes, objects, methods and functions work together.

------------------------------------------------------------
Program Structure
------------------------------------------------------------

main()
│
├── Create Driver objects
│       │
│       ├── driver1
│       └── driver2
│
├── Create Car objects
│       │
│       ├── car1 uses driver1
│       └── car2 uses driver2
│
├── drive(car)
│
├── race(car1, car2)
│
└── park(car)

------------------------------------------------------------
Classes
------------------------------------------------------------

Driver Class
------------

Represents one driver.

Stores information related to a driver.

Example:

Driver
    name
    acceleration
    top_speed
    height

A Driver object DOES NOT know how to drive a car.

It only stores information about the driver.


------------------------------------------------------------

Car Class
---------

Represents one car.

Stores:

- car name
- fuel
- speed
- engine status

The Car also stores a Driver object.

Example:

Car
    car_name
    fuel
    speed
    engine
    driver -------> Driver object

The Car object is responsible for changing its own speed.

The Driver never changes:

    car.speed

directly.

Instead,

Driver
        ↓
Car.accelerate()

changes the speed.

This keeps the object's own data under its control.

------------------------------------------------------------
Relationship Between Objects
------------------------------------------------------------

This project demonstrates a HAS-A relationship.

A Car HAS-A Driver.

Example:

car1
│
├── BMW
├── speed = 20
└── driver
      │
      ├── Arun
      ├── acceleration = 15
      └── top_speed = 180

Instead of copying

driver.name

or

driver.acceleration

inside the Car,

the entire Driver object is stored.

Good:

    self.driver = driver

Bad:

    self.driver_name = driver.name
    self.acceleration = driver.acceleration

Keeping the object itself keeps both objects connected.

------------------------------------------------------------
Methods
------------------------------------------------------------

Methods belong to ONE object.

Example:

car.start()

car.stop()

car.accelerate()

car.status()

These actions only affect one car.

------------------------------------------------------------
Functions
------------------------------------------------------------

Functions coordinate one or more objects.

Example:

drive(car)

park(car)

race(car1, car2)

These are workflows.

They tell multiple objects what to do.

------------------------------------------------------------
Why race() is a function
------------------------------------------------------------

A race is not something one car performs.

A race compares two cars.

Therefore,

def race(car1, car2)

is a better design than

car1.race(car2)

for this learning project.

------------------------------------------------------------
main()
------------------------------------------------------------

main() is the starting point of the program.

Its responsibility is only to:

1. Create objects.
2. Connect objects together.
3. Call functions.
4. Display results.

It should NOT contain business logic.

------------------------------------------------------------
What I Learned
------------------------------------------------------------

✓ Creating classes

✓ Creating objects

✓ __init__()

✓ self

✓ __str__()

✓ Object methods

✓ Functions

✓ Passing objects to functions

✓ Connecting objects together

✓ One object containing another object

✓ Program structure

------------------------------------------------------------
Possible Future Improvements
------------------------------------------------------------

- Fuel consumption
- Engine check
- Maximum speed
- Driver experience
- Car horsepower
- Race class
- Garage class
- Fuel Station class
- Traffic Signal class
- Type hints
- Properties
- Inheritance

============================================================
"""