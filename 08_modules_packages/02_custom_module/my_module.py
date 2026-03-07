"""
--------------------------------------------------
CUSTOM MODULE FILE
File Name: my_module.py
--------------------------------------------------

This file contains reusable math functions.
We will import this file in another Python file.

🧠 What is happening here?

- This file is called a MODULE.
- When another file writes:  import my_module
- Python runs this file once.
- All variables and functions become available.
- We can access them using: my_module.function_name
"""

# A variable inside the module
pi = 3.14


def squar(num):
    """
    Returns square of a number
    """
    return num ** 2


def cube(num):
    """
    Returns cube of a number
    """
    return num ** 3


def circumferance(radius):
    """
    Returns circumference of a circle
    Formula: 2 * pi * radius
    """
    return 2 * pi * radius


def area(radius):
    """
    Returns area of a circle
    Formula: pi * radius^2
    """
    return pi * radius ** 2