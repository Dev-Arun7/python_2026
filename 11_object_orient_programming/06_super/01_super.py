"""
Learning: super()

super() is used inside a child class to access
something from the parent class.

We will learn two important uses of super():

1. super().__init__()
   -> Calls the parent class constructor.

2. super().describe()
   -> Calls the parent class method.

In this example:

             Shape
            /  |  \
           /   |   \
          ↓    ↓    ↓
      Circle Square Triangle

Circle, Square, and Triangle inherit from Shape.
"""


# Parent Class
class Shape:

    # Constructor
    def __init__(self, color, is_filled):

        # Instance Variables
        self.color = color
        self.is_filled = is_filled

    # Method
    def describe(self):

        # Describe the shape
        if self.is_filled:
            print(f"It is {self.color} and filled.")
        else:
            print(f"It is {self.color} and not filled.")


# Circle Class
class Circle(Shape):

    # Constructor
    def __init__(self, color, is_filled, radius):

        # Call the parent class constructor
        # This runs Shape.__init__()
        super().__init__(color, is_filled)

        # Circle's own variable
        self.radius = radius

    # Method overriding
    # Circle creates its own describe() method
    def describe(self):

        # Circle's own description
        area = 3.14 * self.radius * self.radius

        print(f"It is a circle with area of {area} cm^2.")

        # Call the parent class describe() method
        # This is the main use of super() in this example.
        super().describe()


# Square Class
class Square(Shape):

    # Constructor
    def __init__(self, color, is_filled, width):

        # Call the parent class constructor
        super().__init__(color, is_filled)

        # Square's own variable
        self.width = width

    # Method overriding
    def describe(self):

        # Square's own description
        area = self.width * self.width

        print(f"It is a square with area of {area} cm^2.")

        # Call the parent class describe() method
        super().describe()


# Triangle Class
class Triangle(Shape):

    # Constructor
    def __init__(self, color, is_filled, width, height):

        # Call the parent class constructor
        super().__init__(color, is_filled)

        # Triangle's own variables
        self.width = width
        self.height = height

    # Method overriding
    def describe(self):

        # Triangle's own description
        area = 0.5 * self.width * self.height

        print(f"It is a triangle with area of {area} cm^2.")

        # Call the parent class describe() method
        super().describe()


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Creating a Circle object
circle = Circle(color="red", is_filled=True, radius=5)


# Creating a Square object
square = Square(
    color="black",
    is_filled=False,
    width=7
)


# Creating a Triangle object
triangle = Triangle(
    color="blue",
    is_filled=True,
    width=10,
    height=6
)


# ---------------------------------------------------
# Using Circle Object
# ---------------------------------------------------

print("Circle:")

print(f"Color: {circle.color}")
print(f"Filled: {circle.is_filled}")
print(f"Radius: {circle.radius}")

circle.describe()

print()


# ---------------------------------------------------
# Using Square Object
# ---------------------------------------------------

print("Square:")

print(f"Color: {square.color}")
print(f"Filled: {square.is_filled}")
print(f"Width: {square.width}")

square.describe()

print()


# ---------------------------------------------------
# Using Triangle Object
# ---------------------------------------------------

print("Triangle:")

print(f"Color: {triangle.color}")
print(f"Filled: {triangle.is_filled}")
print(f"Width: {triangle.width}")
print(f"Height: {triangle.height}")

triangle.describe()


"""
===================================================
DETAILED NOTE: super()
===================================================

What is super()?
----------------

super() is used inside a child class to access
the parent class.

In simple words:

    super() = "Go to my parent class."


In this example, Shape is the parent class.

Circle, Square, and Triangle are child classes.


---------------------------------------------------
1. super().__init__()
---------------------------------------------------

Look at Circle:

    class Circle(Shape):

        def __init__(self, color, is_filled, radius):

            super().__init__(color, is_filled)

            self.radius = radius


The Circle class needs:

    color
    is_filled
    radius


But color and is_filled already belong to the
parent Shape class.

Instead of writing this again:

    self.color = color
    self.is_filled = is_filled


we can call the parent constructor:

    super().__init__(color, is_filled)


This runs:

    Shape.__init__()


So:

    super().__init__(color, is_filled)

means approximately:

    "Call the __init__() method of my parent."


---------------------------------------------------
Why do we use super() here?
---------------------------------------------------

Without super():

    class Circle(Shape):

        def __init__(self, color, is_filled, radius):

            self.color = color
            self.is_filled = is_filled
            self.radius = radius


This would work.

But we are repeating code that already exists
inside Shape.

Using:

    super().__init__(color, is_filled)

lets the parent class handle its own variables.


---------------------------------------------------
2. super().describe()
---------------------------------------------------

Now look at Circle:

    def describe(self):

        area = 3.14 * self.radius * self.radius

        print(f"It is a circle with area of {area} cm^2.")

        super().describe()


Here Circle has its own describe() method.

This is called:

    Method Overriding


The parent Shape already has:

    describe()


But Circle creates another:

    describe()


When we write:

    circle.describe()

Python uses Circle.describe().

It does NOT automatically run Shape.describe().

That is why we use:

    super().describe()


This tells Python:

    "After running my Circle version,
     also run the parent version."


---------------------------------------------------
The order of execution
---------------------------------------------------

When we call:

    circle.describe()


Python runs:

    Circle.describe()

First:

    print("It is a circle with area...")


Then:

    super().describe()


This calls:

    Shape.describe()


So the final result is:

    Circle's description
           +
    Parent's description


---------------------------------------------------
This is called Extending a Method
---------------------------------------------------

We are not completely replacing the parent method.

We are extending it.

The parent already does:

    describe the color
    describe whether it is filled


Circle adds:

    describe the area


So:

    Circle.describe()

does its own work

AND

    super().describe()

does the parent's work.


The same thing happens in:

    Square.describe()

and:

    Triangle.describe()


---------------------------------------------------
Overriding vs Extending
---------------------------------------------------

Overriding means:

    Child creates its own version
    of the parent method.

Example:

    def describe(self):
        ...


Extending means:

    Child creates its own version
    and also calls the parent version.

Example:

    def describe(self):

        # Child work
        ...

        super().describe()


---------------------------------------------------
super() vs self
---------------------------------------------------

These are different.

self means:

    "This current object."


super() means:

    "My parent class."


For example:

    self.radius

means:

    "Get the radius of this object."


But:

    super().describe()

means:

    "Call describe() from my parent class."


---------------------------------------------------
Example of super() in the constructor
---------------------------------------------------

Parent:

    class Shape:

        def __init__(self, color, is_filled):
            self.color = color
            self.is_filled = is_filled


Child:

    class Circle(Shape):

        def __init__(self, color, is_filled, radius):

            super().__init__(color, is_filled)

            self.radius = radius


The parent handles:

    color
    is_filled


The child handles:

    radius


So each class handles its own responsibility.


---------------------------------------------------
Example of super() with a method
---------------------------------------------------

Parent:

    class Shape:

        def describe(self):
            print("Shape description")


Child:

    class Circle(Shape):

        def describe(self):
            print("Circle description")
            super().describe()


Calling:

    circle.describe()


will produce:

    Circle description
    Shape description


The child runs first.

Then the parent runs because of super().


---------------------------------------------------
Important Point
---------------------------------------------------

super() does NOT mean:

    "Run every parent class."

It refers to the next class in Python's
inheritance order.

In simple single inheritance:

    Child
      ↓
    Parent

super() usually means:

    Parent


Later, when we learn multiple inheritance,
super() becomes more interesting because Python
uses something called:

    MRO

MRO means:

    Method Resolution Order


We will learn this separately.


---------------------------------------------------
Two Main Uses To Remember
---------------------------------------------------

Use 1:

    super().__init__()

Used to call the parent constructor.


Use 2:

    super().method_name()

Used to call a parent method.


So remember:

    super().__init__()
        ↓
    Parent constructor


    super().describe()
        ↓
    Parent describe() method


---------------------------------------------------
Simple Definition
---------------------------------------------------

super() is a Python feature used inside a child
class to access functionality from the parent
class.

In this example:

    super().__init__()

calls the parent constructor.

And:

    super().describe()

calls the parent describe() method.


---------------------------------------------------
Main Idea of This Example
---------------------------------------------------

Shape
  |
  +---- Circle
  |
  +---- Square
  |
  +---- Triangle


The parent Shape contains common properties:

    color
    is_filled

The child classes contain their own properties:

    Circle:
        radius

    Square:
        width

    Triangle:
        width
        height


The child classes also override describe() to
add their own information.

Then they use:

    super().describe()

to keep the common description from Shape.


So we get:

    Child-specific information
              +
    Parent information


This is the main idea you should remember about
super().
"""