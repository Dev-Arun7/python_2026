
"""
What are Type Hints?

Type hints tell us what type of value a variable or function
is expected to use.

They help developers understand code more easily.

Python does NOT automatically enforce type hints at runtime.

Type hints are usually used for:
- Variables
- Function arguments
- Function return values
- Optional values (a value or None)
- Lists and dictionaries
"""

# ---------------------------------------------------
# Example 1: Type hints for variables

print("Example 1: Variables")

# Normal variable
user = "Arun"

# Variable with a type hint
user: str = "Arun"

# int means integer (whole number)
age: int = 25

# float means decimal number
height: float = 170.5

# bool means True or False
is_learning: bool = True

print("User:", user)
print("Age:", age)
print("Height:", height)
print("Is learning:", is_learning)

# Remember:
# user = "Arun" and user: str = "Arun" both work.
# The type hint helps us understand the expected value.


# ---------------------------------------------------
# Example 2: Type hints for function arguments

print("\nExample 2: Function Arguments")


# Without type hints
def greet(name):
    return "Hello " + name


# With type hints
def greet_user(name: str):
    return "Hello " + name


print(greet("Arun"))
print(greet_user("Arun"))

# name: str means name is expected to be a string.
# We can still call greet_user("Arun") normally.


# ---------------------------------------------------
# Example 3: Function return type

print("\nExample 3: Return Type")


# -> int means the function is expected to return an integer.
def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)

print("Result:", result)

# a: int       -> a is expected to be an integer
# b: int       -> b is expected to be an integer
# -> int       -> the function is expected to return an integer
# return       -> sends the result back to the caller


# ---------------------------------------------------
# Example 4: Function that returns nothing

print("\nExample 4: Returning None")


def show_message(message: str) -> None:
    print(message)


show_message("Welcome to Python!")

# -> None means the function is expected not to return
# a meaningful value.
# A function without a return statement returns None.


# ---------------------------------------------------
# Example 5: Type hints for lists

print("\nExample 5: Lists")


# A list of strings
names: list[str] = ["Arun", "Akhil", "Sujatha"]

# A list of integers
numbers: list[int] = [10, 20, 30]

print("Names:", names)
print("Numbers:", numbers)

# list[str] means a list expected to contain strings.
# list[int] means a list expected to contain integers.


# ---------------------------------------------------
# Example 6: Type hints for dictionaries

print("\nExample 6: Dictionaries")


# Dictionary keys are strings.
# Dictionary values are integers.
marks: dict[str, int] = {
    "Arun": 90,
    "Akhil": 85,
}

print("Marks:", marks)

# dict[str, int] means:
# str -> type of the keys
# int -> type of the values


# ---------------------------------------------------
# Example 7: Using str | None

print("\nExample 7: Optional Values")


# The variable can contain a string or None.
user_selected: str | None = None

print("Before selection:", user_selected)

# Later, a user selects something.
user_selected = "Laptop"

print("After selection:", user_selected)

# str | None means the value can be:
# - A string, such as "Laptop"
# - None, meaning no value is available


# ---------------------------------------------------
# Example 8: Optional[str]

print("\nExample 8: Optional Type")


from typing import Optional

# Optional[str] means the same as str | None.
selected_user: Optional[str] = None

print("Selected user:", selected_user)

selected_user = "Arun"

print("Selected user:", selected_user)

# Optional[str] is another way to write str | None.
# The | None syntax is available in Python 3.10 and later.


# ---------------------------------------------------
# Example 9: A function that can return a string or None

print("\nExample 9: Optional Return Type")


def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Arun"

    return None


user = find_user(1)
print("Found user:", user)

user = find_user(2)
print("Found user:", user)

# -> str | None means the function can return:
# - A string
# - None


# ---------------------------------------------------
# Example 10: Type hints do not enforce types automatically

print("\nExample 10: Type Hints Are Not Runtime Checks")


age: int = "twenty"

print("Age:", age)

# This code runs even though age is expected to be an integer.
# Python does not automatically reject the string.
#
# Type hints help developers and tools detect possible mistakes.
# They do not automatically validate values at runtime.


# ---------------------------------------------------
# Summary

"""
Type Hints Summary

str          -> String (text)
int          -> Integer (whole number)
float        -> Decimal number
bool         -> True or False

name: str    -> Variable expected to contain a string
age: int     -> Variable expected to contain an integer

def add(a: int, b: int) -> int:
    -> Arguments are expected to be integers.
    -> The return value is expected to be an integer.

-> None      -> Function is expected not to return a meaningful value.

list[str]    -> List of strings
dict[str, int] -> Dictionary with string keys and integer values

str | None   -> String or None
Optional[str] -> Another way to write str | None

Remember:
Type hints make code easier to understand.
Python does not automatically enforce them at runtime.
"""




# ---------------------------------------------------
# Example 11: What are Annotations?

print("\nExample 11: Annotations")

# An annotation is information attached to a variable.
user: str = "Arun"

print("User:", user)

# user  -> Variable name
# str   -> Annotation
# "Arun" -> Actual value
#
# Here, str is BOTH:
# - An annotation (information written in the code)
# - A type hint (it tells us the expected data type)


# ---------------------------------------------------
# Example 12: What is the Difference Between
# Annotations and Type Hints?

print("\nExample 12: Annotations vs Type Hints")

age: int = 25

print("Age:", age)

# Annotation:
# The information attached to a variable or function.
#
# Type hint:
# An annotation used to indicate the expected data type.
#
# In this example, int is BOTH an annotation and a type hint.
#
# Remember:
# Annotation describes how the information is written.
# Type hint describes the purpose of that information.


# ---------------------------------------------------
# Example 13: Function Annotations

print("\nExample 13: Function Annotations")


def add(a: int, b: int) -> int:
    return a + b


print("Result:", add(10, 20))

# a: int -> Annotation for argument a
# b: int -> Annotation for argument b
# -> int  -> Annotation for the return value
#
# These are also type hints because they indicate
# the expected types of the arguments and return value.


# ---------------------------------------------------
# Example 14: Annotations Are Not Always Type Hints

print("\nExample 14: Other Annotations")


def greet(name: str) -> str:
    return f"Hello {name}"


print(greet("Arun"))

# Here, str is an annotation and a type hint.
#
# Python annotations can technically contain other values,
# but using descriptions like "person's name" instead of
# str is not recommended in normal Python code.
#
# For beginners, focus on type hints such as str, int and bool.

# ---------------------------------------------------
# Example 15: Checking Function Annotations

print("\nExample 15: Checking Annotations")


def multiply(a: int, b: int) -> int:
    return a * b


print(multiply.__annotations__)

# __annotations__ stores the annotations of a function.
#
# The output will be similar to:
# {'a': <class 'int'>, 'b': <class 'int'>,
#  'return': <class 'int'>}
#
# This is useful when learning how Python stores annotations.
# You do not need to use __annotations__ in everyday coding.


# ---------------------------------------------------
# Example 16: Type Hints Do Not Enforce Types

print("\nExample 16: Type Hints Are Not Enforced Automatically")


def show_age(age: int) -> int:
    return age


print(show_age("twenty"))

# Although age is annotated as int, Python still allows
# us to pass a string during a normal function call.
#
# Type hints do not automatically validate the value.
# A type checker can detect this potential mistake.
#
# IMPORTANT:
# This example deliberately passes the wrong type.
# Do not use this pattern in normal code.


# ---------------------------------------------------
# Final Summary

"""
ANNOTATIONS AND TYPE HINTS

1. Annotation:
   Information attached to a variable or function.

2. Type hint:
   An annotation used to indicate the expected data type.

3. Example:
   user: str = "Arun"

   user -> Variable name
   str  -> Annotation and type hint
   "Arun" -> Actual value

4. Function example:
   def add(a: int, b: int) -> int:
       return a + b

   a: int -> Argument annotation and type hint
   b: int -> Argument annotation and type hint
   -> int -> Return annotation and type hint

5. Not every annotation is a type hint.
   An annotation can contain other information too.

6. Type hints do not automatically enforce types at runtime.

7. Python tools, such as type checkers, can use type hints
   to detect potential mistakes.

Remember:
Annotations are the broader concept.
Type hints are one common use of annotations.
"""
