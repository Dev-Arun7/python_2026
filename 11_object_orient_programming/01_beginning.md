# OOP Core Concepts – Class, Object, Constructor, Methods

In this file, we will understand the core concepts of OOP using a Car example.

We will learn:

- Class
- Object
- Constructor
- Methods

Do not worry. Everything is simple.

---

## 1. The Car Example

Think about a car.

A car has:

Data (Properties):
- color
- year
- fuel
- model

Actions (Behaviors):
- start()
- stop()
- show_details()

In OOP:

- Data → Variables
- Actions → Functions
- Car → Class
- My car → Object

---

## 2. What is a Class?

A class is a blueprint.

It defines what a car should have.

Example structure:

class Car:
    pass

Right now, this class does nothing.
It is just a blueprint.

---

## 3. What is an Object?

An object is a real car created from the class.

Example:

my_car = Car()

Here:

- Car → Class (blueprint)
- my_car → Object (real car)

You can create many objects:

car1 = Car()
car2 = Car()
car3 = Car()

All are created from the same blueprint.

---

## 4. Adding Data to a Class (Constructor)

Now we want each car to have:

- color
- year
- fuel
- model

We use something called a constructor.

A constructor is a special function that runs automatically when an object is created.

It is written as:

__init__

Example:

class Car:

    def __init__(self, color, year, fuel, model):
        self.color = color
        self.year = year
        self.fuel = fuel
        self.model = model

Now when we create a car:

car1 = Car("Red", 2022, "Petrol", "Toyota")

This car has its own data.

---

## 5. What is self?

self refers to the current object.

If we create:

car1 = Car("Red", 2022, "Petrol", "Toyota")
car2 = Car("Blue", 2020, "Diesel", "Honda")

Then:

car1.color → Red
car2.color → Blue

self helps Python understand which object we are talking about.

---

## 6. Adding Methods (Functions Inside Class)

Now let’s add actions.

Example:

class Car:

    def __init__(self, color, year, fuel, model):
        self.color = color
        self.year = year
        self.fuel = fuel
        self.model = model

    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

    def show_details(self):
        print("Color:", self.color)
        print("Year:", self.year)
        print("Fuel:", self.fuel)
        print("Model:", self.model)

Now we can use:

car1 = Car("Red", 2022, "Petrol", "Toyota")

car1.start()
car1.show_details()
car1.stop()

---

## 7. Important Understanding

Class → Blueprint  
Object → Real thing created from blueprint  
Constructor → Runs automatically when object is created  
Method → Function inside class  

---

## 8. Why This Is Better

Instead of creating many separate variables like:

color1, year1, fuel1, model1  
color2, year2, fuel2, model2  

We now create:

car1  
car2  

Everything related to that car stays inside that object.

This makes code:

- Clean
- Organized
- Easy to understand

---

## 9. What We Will Learn Next

Now that you understand:

- Class
- Object
- Constructor
- Methods

Next we will write actual Python files:

- class_object.py
- constructor.py
- methods.py

With step-by-step beginner examples.