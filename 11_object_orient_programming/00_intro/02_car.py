"""
In this file we learn:

1. What is a Class
2. What is an Object
3. How to create objects from a class
4. How to access object attributes

We will use a Car example.
"""


# ---------------------------------------------------
# Step 1: Creating a Class

# A class is like a blueprint.
# It defines what properties a car should have.

class Car:
    # Constructor  
    # __init__ is a special method called a constructor.
    # It runs automatically when a new object is created.

    def __init__(self, model, year, color, for_sale):
        # self refers to the current object
        # These are attributes (variables inside the object)
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale



# ---------------------------------------------------
# Step 2: Creating an Object

# Creating our first car object
car_1 = Car("Mustang", 2024, "white", True)   # I dont like a white car 😁, so selling = True 


# ---------------------------------------------------
# Accessing object attributes

print("Car 1 Model:", car_1.model)
print("Car 1 Year:", car_1.year)
print("Car 1 Color:", car_1.color)
print("Car 1 For Sale:", car_1.for_sale)

print()


# ---------------------------------------------------
# Example 2: Creating another object

car_2 = Car("BMW M3", 2022, "black", False)

print("Car 2 Model:", car_2.model)
print("Car 2 Year:", car_2.year)
print("Car 2 Color:", car_2.color)
print("Car 2 For Sale:", car_2.for_sale)

print()


# ---------------------------------------------------
# Example 3: Creating object using keyword arguments

# Here we specify parameter names.
# So the order does not matter.

car_3 = Car(model="Toyota Supra", year=2023, color="red", for_sale=True)

print("Car 3 Model:", car_3.model)
print("Car 3 Year:", car_3.year)
print("Car 3 Color:", car_3.color)
print("Car 3 For Sale:", car_3.for_sale)

print()


# ---------------------------------------------------
# Example 4: Using object attributes in a condition

if car_1.for_sale:
    print(car_1.model, "is available for sale")
else:
    print(car_1.model, "is not for sale")

print()


# ---------------------------------------------------
# Example 5: Using objects inside a loop

# We can store objects inside a list

cars = [car_1, car_2, car_3]

print("Listing all cars:")

for car in cars:
    print(car.model, "-", car.color, "-", car.year)


print("\nProgram finished successfully 🚗")



