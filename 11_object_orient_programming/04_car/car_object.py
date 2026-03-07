"""
This script imports the Car class
and creates objects from it.

Then we call different methods of the class.
"""

from car import Car


# ---------------------------------------------------
# Creating objects

car_1 = Car("Mustang", 2024, "white", True)
car_2 = Car("BMW M3", 2022, "black", False)
car_3 = Car("Toyota Supra", 2023, "red", True)


# ---------------------------------------------------
# Calling methods

print("===== Car 1 =====")
car_1.describe()
car_1.drive()
car_1.stop()

print("\n===== Car 2 =====")
car_2.describe()
car_2.drive()
car_2.stop()

print("\n===== Car 3 =====")
car_3.describe()
car_3.drive()
car_3.stop()


# ---------------------------------------------------
# Using objects inside a loop

print("\n===== All Cars =====")

cars = [car_1, car_2, car_3]

for car in cars:
    car.describe()
    print("-" * 40)