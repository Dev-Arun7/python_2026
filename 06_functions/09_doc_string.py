"""
--------------------------------------------------
DOCSTRING IN PYTHON
--------------------------------------------------

Docstring = Documentation String

It is used to describe:
- What a module does
- What a function does
- What a class does

Docstring is written inside triple quotes:
"""  """   or   '''  '''

It is placed immediately below:
- Module
- Function definition
- Class definition
"""
# --------------------------------------------------
# Function with Docstring
# --------------------------------------------------

def add_numbers(a, b):
    """
    Adds two numbers and returns the result.

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: Sum of a and b
    """
    result = a + b
    return result


# --------------------------------------------------
# Calling the Function
# --------------------------------------------------

print("Result:", add_numbers(10, 5))


# --------------------------------------------------
# Accessing the Docstring
# --------------------------------------------------

print("\nAccessing Docstring using __doc__ :")
print(add_numbers.__doc__)


# --------------------------------------------------
# Using help() function
# --------------------------------------------------

print("\nUsing help() function:")
help(add_numbers)