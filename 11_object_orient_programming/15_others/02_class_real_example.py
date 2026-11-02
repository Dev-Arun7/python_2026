
"""
Learning: OOP - Putting Everything Together

In this example, we are building a simple Car Racing
simulation.

We are using multiple OOP concepts together:

    1. Classes and Objects
    2. Constructors (__init__)
    3. Inheritance
    4. Encapsulation (organizing data and methods)
    5. Composition
    6. Polymorphism (__str__ method)
    7. Methods and Object Interaction

We have three main classes:

    Vehicle
       |
       ↓
      Car

    Driver


A Car is a Vehicle.

A Car also HAS a Driver.

The Driver and Car objects work together
to simulate a small racing game.

Note:
This is a simple learning simulation, not a
realistic car or racing system.
"""


import random


# ---------------------------------------------------
# Vehicle Class
# ---------------------------------------------------

# Parent class
class Vehicle:

    def __init__(self, driver):

        # Store the Driver object inside the Vehicle
        self.driver = driver

        # Initial vehicle values
        self.engine = False
        self.speed = 0
        self.temperature = 0

        # Give each vehicle a random maximum speed
        self.max_speed = random.randint(75, 150)

    # Start the engine
    def start_engine(self):

        if not self.engine:
            self.engine = True
        else:
            print("Engine is already running...")

    # Increase vehicle speed
    def accelerate_engine(self):

        # Acceleration is possible only when the engine is running
        if self.engine:

            # Driver's fitness affects acceleration
            self.speed += random.randint(
                1, self.driver.max_acceleration
            )

            # Increase engine temperature
            self.temperature += random.randint(10, 30)

            # Do not allow speed to exceed the maximum
            if self.speed > self.max_speed:
                self.speed = self.max_speed
                print("Max speed reached")

        else:
            print("Engine is off...! Please start the engine first")

    # Reduce vehicle speed
    def break_car(self):

        self.speed -= random.randint(3, 10)

        # Speed should never become negative
        if self.speed < 0:
            self.speed = 0

    # Stop and park the vehicle
    def park_car(self):

        if not self.engine:
            print("Car already off...")
            return

        self.speed = 0
        self.engine = False
        self.temperature = 0

        print("Car parked...")


# ---------------------------------------------------
# Car Class
# ---------------------------------------------------

# Car inherits from Vehicle
class Car(Vehicle):

    def __init__(self, car_name, driver):

        # Call the parent class constructor
        super().__init__(driver)

        self.car_name = car_name

    # Return a readable string when printing a Car object
    def __str__(self):
        return f"{self.car_name} | {self.driver.name}"

    # Increase the car's maximum speed
    def modify_max_speed(self):
        self.max_speed += 5


# ---------------------------------------------------
# Driver Class
# ---------------------------------------------------

class Driver:

    def __init__(self, driver_name):

        self.name = driver_name

        # Give each driver random initial values
        self.max_acceleration = random.randint(5, 20)
        self.weight = random.randint(70, 110)

    # Return the driver's name when printing the object
    def __str__(self):
        return f"{self.name}"

    # Workout improves the driver's acceleration
    def workout(self):

        self.max_acceleration += 1
        self.weight -= 2

        print(f"Driver acceleration increased....: {self.max_acceleration}")

    # Eating junk food affects the driver's performance
    def eat_junk(self):

        self.weight += 3
        self.max_acceleration -= 1


# ---------------------------------------------------
# Race Function
# ---------------------------------------------------

# Compare the speeds of two cars
def race(car1, car2):

    if car1.speed > car2.speed:
        return car1.car_name

    if car2.speed > car1.speed:
        return car2.car_name

    return "DRAW......"


# ---------------------------------------------------
# Main Function
# ---------------------------------------------------

def main():

    # Create two Driver objects
    driver1 = Driver("Arun")
    driver2 = Driver("Anila")

    # Create two Car objects and assign their drivers
    car1 = Car("BMW", driver1)
    car2 = Car("Audi", driver2)

    # Driver activities
    driver1.workout()
    driver1.workout()
    driver1.eat_junk()

    driver2.eat_junk()

    # Modify Audi's maximum speed
    car2.modify_max_speed()

    # Start and accelerate the cars
    car1.start_engine()

    car2.accelerate_engine()  # Engine is still off
    car2.start_engine()

    car2.accelerate_engine()
    car2.accelerate_engine()

    car1.accelerate_engine()
    car1.accelerate_engine()

    # Reduce the speed of both cars
    car1.break_car()
    car2.break_car()

    # Compare the car speeds
    result = race(car1, car2)

    # Park both cars
    car1.park_car()
    car2.park_car()

    print(f"Winner is: {result}")


# Execute main() only when this file is run directly
if __name__ == "__main__":
    main()


"""
===================================================
SHORT NOTE: OOP CONCEPTS USED
===================================================

1. Classes and Objects
   Vehicle, Car and Driver are classes.
   We create objects using these classes.

2. Inheritance
   Car inherits from Vehicle.

   class Car(Vehicle):

3. Composition
   Vehicle contains a Driver object.

   self.driver = driver

4. Encapsulation
   Each class keeps related data and methods together.

5. Polymorphism
   __str__() provides a readable string representation
   of different objects.

6. Constructors
   __init__() initializes objects when they are created.

7. Object Interaction
   Car uses Driver information to calculate acceleration.

8. Functions
   race() compares two Car objects and returns the winner.


MAIN IDEA
---------

Real-world applications rarely use only one OOP concept.

Different concepts work together to build a complete
program.

This example combines the OOP concepts we have learned
so far into one small project.
"""
