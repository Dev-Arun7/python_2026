# Python OOP: Composition

## 1. What is Composition?

Composition is an Object-Oriented Programming (OOP) concept.

It means:

> One object contains and uses another object.

In simple words, a class can use objects created from other classes to
do its work.

For example:

-   A car has an engine.
-   A car has a fuel tank.
-   A computer has a processor.
-   A house has rooms.

These are examples of **HAS-A relationships**.

## 2. A Simple Real-World Example

Think about a car.

A car needs different parts to work:

-   An engine to produce power.
-   A fuel tank to store fuel.
-   A battery to provide electrical power.

Each part has its own job.

We can represent this idea using separate Python classes.

``` text
             Car
          /   |    \
         /    |     \
        v     v      v
     Engine Fuel Tank Battery
```

The `Car` object brings these objects together and uses them when
needed.

## 3. Why Do We Need Composition?

Imagine writing a car program without separate classes.

We might put everything into one large `Car` class:

``` text
Car
 |
 |-- engine details
 |-- engine operations
 |-- fuel tank details
 |-- fuel operations
 |-- battery details
 |-- battery operations
 |-- car operations
```

As the program grows, this class can become difficult to understand and
maintain.

Instead, we can divide the work into smaller classes.

``` text
Engine
  - manufacturer
  - horsepower
  - start_engine()

Fuel_Tank
  - capacity
  - fuel
  - refuel()

Car
  - brand
  - model
  - start_car()
  - drive_car()
```

Each class has a clear responsibility.

This makes our code easier to:

-   Read and understand.
-   Maintain and update.
-   Reuse in other parts of a program.
-   Test and find problems in.

## 4. How Does Composition Work in Python?

First, create an object from another class:

``` python
engine1 = Engine("BMW", 150)
```

Now `engine1` is an `Engine` object.

We can pass that object to the `Car` constructor:

``` python
car1 = Car("BMW", "X5", engine1)
```

The `Car` class can receive and store it:

``` python
class Car:
    def __init__(self, brand, model, engine):
        self.brand = brand
        self.model = model

        # Store the Engine object inside the Car object
        self.engine = engine
```

The important line is:

``` python
self.engine = engine
```

Here:

-   `engine` is the object received by the constructor.
-   `self.engine` stores a reference to that object.
-   The `Car` object can now use the Engine object.

For example:

``` python
self.engine.start_engine()
```

This calls the `start_engine()` method of the Engine object.

## 5. The Object Relationship

The relationship can be pictured like this:

``` text
engine1 = Engine(...)
       |
       v
   Engine object
       ^
       |
   car1.engine
       ^
       |
    Car object
```

The `Car` object does not copy all the engine code.

It keeps a reference to the Engine object and uses it.

A car can also contain more than one object:

``` text
             car1
              |
        +-----+------+
        |            |
        v            v
     engine1     fuel_tank1
        |            |
        v            v
     Engine       Fuel_Tank
```

This is the idea used in the two Composition examples that follow.

## 6. Composition vs Inheritance

Composition and inheritance are different ways to connect classes.

### Inheritance: IS-A relationship

A child class is a type of its parent class.

Example:

``` python
class Animal:
    pass

class Dog(Animal):
    pass
```

A Dog **is an** Animal.

### Composition: HAS-A relationship

An object contains or uses another object.

Example:

``` python
class Car:
    def __init__(self, engine):
        self.engine = engine
```

A Car **has an** Engine.

Remember:

  -----------------------------------------------------------------------
  Inheritance                         Composition
  ----------------------------------- -----------------------------------
  IS-A relationship                   HAS-A relationship

  A class inherits from another class An object contains or uses another
                                      object

  `class Dog(Animal):`                `self.engine = engine`
  -----------------------------------------------------------------------

## 7. One Important Difference: Composition and Aggregation

You may sometimes see the word **Aggregation** when learning OOP.

Both aggregation and composition describe HAS-A relationships.

A simple distinction:

-   **Aggregation:** The contained object can exist independently of the
    object using it.
-   **Composition:** The containing object has stronger ownership of the
    contained object; its lifecycle is usually tied to the owner.

In our beginner examples, the Engine and Fuel_Tank objects are created
separately and passed into the Car.

So, technically, these examples are closer to aggregation in the strict
OOP definition.

For now, focus on the main idea: one object can store and use another
object. The ownership distinction can be learned later.

## 8. When Should We Use Composition?

Composition is useful when:

-   One object needs the work or data of another object.
-   Different parts of a program have separate responsibilities.
-   We want to avoid putting too much code in one class.
-   We want to reuse objects in different places.

For example, an online shopping application might have:

``` text
Order
 |
 +-- Customer
 |
 +-- Payment
 |
 +-- Delivery
```

The Order object can work with Customer, Payment, and Delivery objects.

## 9. Main Takeaway

Composition allows us to build larger objects using smaller objects.

Instead of making one class responsible for everything:

1.  Create separate classes for separate responsibilities.
2.  Create objects from those classes.
3.  Pass the objects where they are needed.
4.  Store and use those objects inside another object.

**Remember:**

> Composition is about building objects that work together.

In the next examples, we will start with a Car that has an Engine, and
then extend it to a Car that has both an Engine and a Fuel Tank.
