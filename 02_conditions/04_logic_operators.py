"""
Logical Operators in Python
---------------------------
Logical operators are used to combine or reverse conditions.

Python has 3 logical operators:

1. and
2. or
3. not
"""

# ============================================================================
# AND OPERATOR
# ============================================================================
# The "and" operator returns True only if BOTH conditions are True.
#
# True  and True   -> True
# True  and False  -> False
# False and True   -> False
# False and False  -> False

print("========== AND OPERATOR ==========")

age = 20
balance = 1000

# Both conditions must be True
if age >= 18 and balance >= 500:
    print("You can buy the product!")
else:
    print("Access denied!")

print()

# ----------------------------------------------------------------------------
# Example 2
# ----------------------------------------------------------------------------

marks = 85
attendance = 92

# Student must have good marks AND good attendance
if marks >= 50 and attendance >= 75:
    print("You passed the course!")
else:
    print("You failed the course!")

print()

# ============================================================================
# OR OPERATOR
# ============================================================================
# The "or" operator returns True if AT LEAST ONE condition is True.
#
# True  or True   -> True
# True  or False  -> True
# False or True   -> True
# False or False  -> False

print("========== OR OPERATOR ==========")

ticket = False
vip = True

# Only one condition needs to be True
if ticket or vip:
    print("You can enter the event!")
else:
    print("Entry denied!")

print()

# ----------------------------------------------------------------------------
# Example 2
# ----------------------------------------------------------------------------

weekend = False
holiday = True

# If today is weekend OR holiday, you can relax
if weekend or holiday:
    print("You can relax today!")
else:
    print("Go to work!")

print()

# ============================================================================
# NOT OPERATOR
# ============================================================================
# The "not" operator reverses the result.
#
# not True  -> False
# not False -> True

print("========== NOT OPERATOR ==========")

is_raining = False

# "not" changes False to True
if not is_raining:
    print("Go outside!")
else:
    print("Stay inside!")

print()

# ----------------------------------------------------------------------------
# Example 2
# ----------------------------------------------------------------------------

logged_in = False

# User is NOT logged in
if not logged_in:
    print("Please login first!")
else:
    print("Welcome back!")

print()

# ============================================================================
# COMBINING LOGICAL OPERATORS
# ============================================================================
# You can also combine multiple logical operators together.

print("========== COMBINED EXAMPLE ==========")

age = 20
money = 400
student = False

# Person must be 18 or older AND have enough money
if age >= 18 and money >= 300:
    print("You can buy the movie ticket!")
else:
    print("You cannot buy the movie ticket!")

# Either adult OR student can enter
if age >= 18 or student:
    print("You can enter the library!")
else:
    print("Entry denied!")

# Reverse the value of student
if not student:
    print("You are not a student.")
else:
    print("You are a student.")