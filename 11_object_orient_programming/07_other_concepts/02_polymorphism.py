"""
Learning: Polymorphism

Polymorphism means:

    "One interface, different behavior."

In this example, all shapes have an area() method.

But each shape calculates its area differently.

        Shape
       /  |  \
      /   |   \
     ↓    ↓    ↓
 Circle Square Triangle
     ↑
     |
   Pizza

Pizza inherits from Circle.

The important part is:

    shape.area()

The same method call works with different objects.
"""

# Importing Abstract Class Tools

from abc import ABC, abstractmethod


# Parent Class
class Shape(ABC):

    # Abstract method
    # Every shape 'must' provide its own area() method, here it is a pass
    @abstractmethod
    def area(self):
        pass


# Circle inherits from Shape
class Circle(Shape):

    # Constructor
    def __init__(self, radius):

        # Circle's own variable
        self.radius = radius

    # Circle's implementation of area()
    def area(self):
        return 3.14 * self.radius ** 2


# Square inherits from Shape
class Square(Shape):

    # Constructor
    def __init__(self, side):

        # Square's own variable
        self.side = side

    # Square's implementation of area()
    def area(self):
        return self.side ** 2


# Triangle inherits from Shape
class Triangle(Shape):

    # Constructor
    def __init__(self, base, height):

        # Triangle's own variables
        self.base = base
        self.height = height

    # Triangle's implementation of area()
    def area(self):
        return self.base * self.height * 0.5


# Pizza inherits from Circle
class Pizza(Circle):

    # Constructor
    def __init__(self, radius, topping):

        # Call the Circle constructor
        super().__init__(radius)

        # Pizza's own variable
        self.topping = topping


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Creating different Shape objects
shapes = [
    Circle(4),
    Square(5),
    Triangle(6, 7),
    Pizza(15, "Pepperoni")
]


# ---------------------------------------------------
# Polymorphism
# ---------------------------------------------------

# The same code works with different objects
for shape in shapes:

    # Each object uses its own area() method
    print(f"Area is {shape.area()}")




"""
===================================================
DETAILED NOTE: POLYMORPHISM
===================================================

What is Polymorphism?
---------------------

Polymorphism means:

    Same method
    +
    Different behavior


In this example, all Shape classes have:

    area()


But each class calculates the area differently.


---------------------------------------------------
Different area() Methods
---------------------------------------------------

Circle:

    area() -> 3.14 * radius ** 2


Square:

    area() -> side ** 2


Triangle:

    area() -> base * height * 0.5


So all of them have the same method name:

    area()

But the implementation is different.


---------------------------------------------------
Where is Polymorphism Happening?
---------------------------------------------------

Look at this:

    shapes = [
        Circle(4),
        Square(5),
        Triangle(6, 7),
        Pizza(15, "Pepperoni")
    ]


Then:

    for shape in shapes:
        print(shape.area())


We are using the exact same code:

    shape.area()


But Python calls the correct method based on
the object.


For example:

    Circle object
        ↓
    Circle.area()


    Square object
        ↓
    Square.area()


    Triangle object
        ↓
    Triangle.area()


---------------------------------------------------
Pizza
---------------------------------------------------

Pizza inherits from Circle:

    class Pizza(Circle):

So Pizza gets the area() method from Circle.

Pizza does not create its own area() method.

Therefore:

    Pizza.area()

uses:

    Circle.area()


The Pizza object can still be used in the same
loop because it has an area() method.


---------------------------------------------------
Why is this useful?
---------------------------------------------------

We don't need to write separate code like:

    if it is Circle:
        ...


    if it is Square:
        ...


    if it is Triangle:
        ...


Instead, we can simply write:

    shape.area()


Each object takes care of its own behavior.


---------------------------------------------------
Abstract Method
---------------------------------------------------

Shape defines:

    @abstractmethod
    def area(self):
        pass


This tells child classes:

    "Every Shape must have an area() method."

Circle, Square, and Triangle must therefore
implement area().


This gives us a common structure for all shapes.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Polymorphism means:

    The same method call can behave differently
    depending on the object.


In this example:

    shape.area()


can produce different results for:

    Circle
    Square
    Triangle
    Pizza


---------------------------------------------------
Main Idea
---------------------------------------------------

Instead of asking:

    "What type of object is this?"


We can simply say:

    "Call area()."


The object itself provides the correct behavior.

That is the main idea of polymorphism.
"""