"""
car.py

This file contains the Car class definition.

The class acts like a blueprint.
Other Python files can import this class and create car objects.
"""


class Car:

    # Constructor
    # This runs automatically when a new object is created
    def __init__(self, model, year, color, for_sale):

        # 'self' refers to the current object

        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # ---------------------------------------------------
    # Method: describe the car

    def describe(self):
        print(f"A {self.color} {self.model} released in {self.year}")

        if self.for_sale:
            print("Available for sale")
        else:
            print("Not available for sale")

    # ---------------------------------------------------
    # Method: drive the car

    def drive(self):
        print(f"You drive the {self.color} {self.model}")

    # ---------------------------------------------------
    # Method: stop the car

    def stop(self):
        print(f"You stop the {self.color} {self.model}")