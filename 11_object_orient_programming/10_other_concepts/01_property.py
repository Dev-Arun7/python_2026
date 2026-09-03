"""
@property in Python

@property allows us to use a method like an attribute.

It is useful when we want to add extra logic when an attribute
is read, changed, or deleted.

Using @property, we can create:
    - Getter  -> Get/read a value
    - Setter  -> Set/change a value
    - Deleter -> Delete a value
"""


class Rectangle:
    """
    A simple Rectangle class demonstrating @property,
    getter, setter, and deleter.
    """

    def __init__(self, width, height):
        self._width = width
        self._height = height

    # Getter for width
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    # Getter for height
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    # Setter for width
    # We can validate the value before storing it.
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero.")

    # Setter for height, logic for validation is there.
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero.")

    # Deleter for width
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")

    # Deleter for height
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted!")


# Create a Rectangle object
rectangle = Rectangle(3, 4)

# Setter rejects this value because it is less than or equal to zero
rectangle.width = -2

# Setter accepts this value
rectangle.width = 2

# Setter accepts this value
rectangle.height = 5

# Getter is automatically called here
print(rectangle.width)
print(rectangle.height)


"""
NOTES
-----

1. Getter
---------

When we write:

    rectangle.width

Python automatically calls:

    @property
    def width(self):


2. Setter
---------

When we write:

    rectangle.width = 2

Python automatically calls:

    @width.setter
    def width(self, new_width):

This allows us to validate the value before saving it.


3. Deleter
----------

When we write:

    del rectangle.width

Python automatically calls:

    @width.deleter
    def width(self):


4. Why use @property?
---------------------

Without @property, we could directly change the value:

    rectangle.width = -10

There would be no validation.

With @property, we can control what happens when the
attribute is read, changed, or deleted.


5. What does _width mean?
-------------------------

The underscore in:

    self._width

is a naming convention.

It means:

    "This attribute is intended for internal use."

It is NOT completely private. Python still allows us to access it:

    rectangle._width

So it is better to think of _width as an internal attribute.


Simple idea:

    rectangle.width
          |
          v
        Getter
          |
          v
       _width


    rectangle.width = 5
          |
          v
        Setter
          |
          v
       Validation
          |
          v
       _width = 5


The main benefit of @property is:

We can make an attribute simple to use while still
controlling what happens behind the scenes.
"""