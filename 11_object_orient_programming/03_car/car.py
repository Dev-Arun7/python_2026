"""
car.py

This file contains the class definition.

We define the Car blueprint here.
Other Python files can import and use this class.
"""


class Car:

    # Constructor
    # Runs automatically when a new Car object is created
    def __init__(self, model, year, color, for_sale):

        # self refers to the current object

        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale