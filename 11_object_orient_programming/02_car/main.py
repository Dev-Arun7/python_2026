"""
In this script we import the Car class from another file
and create objects from it.

This shows how classes can be reused across files.
The code looks more clean as well
"""

# Import the class from car.py
from car import Car


# ---------------------------------------------------
# Creating objects

# Create 3 car objects
car_1 = Car("Mustang", 2024, "white", True)
car_2 = Car("BMW M3", 2022, "black", False)

# Using keyword arguments (order does not matter)
car_3 = Car(model="Toyota Supra", year=2023, color="red", for_sale=True)


# ---------------------------------------------------
# Example 1: Accessing object attributes

print(f"========== {car_1.model} ==========")

if car_1.for_sale:
    print(f"{car_1.model} car is {car_1.color} in color and {car_1.year}")
    print(f"{car_1.model} is available for sale...!")
else:
    print(f"{car_1.model} is not for sale")

print("-" * 70)


# ---------------------------------------------------
# Example 2: Using objects inside a loop

# Store all objects inside a list
cars = [car_1, car_2, car_3]

print("Listing all cars:\n")

for car in cars:

    print(f"{car.model} - {car.year} - {car.color}")

    if car.for_sale:
        print("It is available for sale")

    print("-" * 70)





