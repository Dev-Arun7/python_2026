"""
====================================================
FUNCTIONS WITH ARGUMENTS (BEGINNER FRIENDLY)
====================================================

What is an argument?

Argument = The value we send into a function.

Example:
    happy_birthday("Arun")

Here "Arun" is the argument.

Parameter = The variable that receives the value
inside the function.

Now let's understand step by step.
"""

# ====================================================
# 1️⃣ Function With ONE Argument
# ====================================================

def happy_birthday(person):
    # "person" is a parameter
    # It receives the value we send

    print(f"Happy birthday {person}...")
    print("Happy birthday to you!")
    print()


# Calling the function using a variable
name = "Arun"
happy_birthday(name)

# Calling directly without variable
happy_birthday("Akhil")
happy_birthday("Anila")


# ====================================================
# 2️⃣ Function With TWO Arguments
# ====================================================

def happy_birthday_2(person, age):

    print(f"Happy birthday {person}.")
    print(f"You are {age} years old now.")
    print("Happy birthday to you.")
    print()


person = "Anila"
age = 22

happy_birthday_2(person, age)


# ====================================================
# ⚠ Order of Arguments is Important
# ====================================================

# Correct order
happy_birthday_2("Rahul", 30)

# Wrong order (will run, but output meaning is wrong)
# happy_birthday_2(30, "Rahul")


# ====================================================
# ⚠ Wrong Number of Arguments Causes Error
# ====================================================

person = "Akhil"
age = 25
place = "London"

# This will cause error because function expects only 2 values
# happy_birthday_2(person, age, place)


# ====================================================
# 3️⃣ Another Simple Example
# ====================================================

def greet(name):
    print(f"Hello {name}!")
    print()

greet("Arun")
greet("Gayatri")
greet("Bro")


# ====================================================
# IMPORTANT NOTE
# ====================================================
# 1. Function is created once.
# 2. We can call it many times.
# 3. Arguments make the function flexible.
# 4. Same function can work with different values.
#
# Think like a machine:
# If you send different input,
# you get different output.
#
# That is the power of arguments in functions.
# ====================================================