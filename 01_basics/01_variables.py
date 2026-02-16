"""
File: 01_basics/variables.py
Topic: Variables (Beginner)

Goal:
- Understand what a variable is in Python
- Learn how assignment works
- Print values to the console

You will learn:
1) Creating variables
2) Re-assigning variables
3) Naming rules (quick intro)

Run:
python 01_basics/variables.py
"""

# ----------------------------
# 1) Creating variables
# ----------------------------
name = "Arun"
age = 25

print("Name:", name)
print("Age:", age)

# ----------------------------
# 2) Re-assigning variables
# ----------------------------
age = 26
print("Updated age:", age)

# ----------------------------
# 3) Naming rules (quick intro)
# ----------------------------
# ✅ Good:
user_name = "my_lord"

# ❌ Bad (don’t do these):
# 2name = "x"      # cannot start with a number
# user-name = "x"  # '-' is not allowed in variable names



# F strings (f"string") allow us to embed variables directly in strings
print(f"My name is {name} and I am {age} years old.")




# Different types of variables (we will learn about these in the next lesson)
# Strings, Integers, Floats, Booleans






# ----------------------------
# Practice (do it yourself)
# ----------------------------
# TODO 1: Create a variable 'city' and assign your city name
# TODO 2: Print: "I live in <city>"
# TODO 3: Change city to a different value and print again
