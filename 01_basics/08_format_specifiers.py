"""
Goal:
- Learn how to format strings
- Understand % formatting
- Learn .format() method
- Learn f-strings (recommended)
"""

# ----------------------------
# 1) What is string formatting?
# ----------------------------
# String formatting means inserting values into a string

name = "Arun"
age = 33

print("My name is", name, "and I am", age, "years old")


# ----------------------------
# 2) Old style formatting (%)
# ----------------------------
# %s -> string
# %d -> integer
# %f -> float

price = 19.99

print("Name: %s" % name)
print("Age: %d" % age)
print("Price: %f" % price)

# limiting float to 2 decimal places
print("Price: %.2f" % price)


# ----------------------------
# 3) format() method
# ----------------------------
# {} placeholders

print("My name is {} and I am {} years old".format(name, age))

# with positions
print("Age: {1}, Name: {0}".format(name, age))

# formatting float
print("Price: {:.2f}".format(price))

# I suggest you to ignore above formating since the best way it below. :)

# ----------------------------
# 4) f-strings (BEST & MODERN)
# ----------------------------
# easiest and most readable 🙂

print(f"My name is {name} and I am {age} years old")

# expressions inside f-string
num1 = 10
num2 = 5

print(f"Sum of {num1} + {num2} = {num1 + num2}")

# float formatting
print(f"Price: {price:.2f}")


# ----------------------------
# 5) Aligning text
# ----------------------------
# < left align
# > right align
# ^ center

word = "Python"

print(f"|{word:<10}|")  # left
print(f"|{word:>10}|")  # right
print(f"|{word:^10}|")  # center


# ----------------------------
# 6) TODO Practice
# ----------------------------
# TODO: Create variables city and temperature
# Print: "City: Mumbai, Temp: 30.50°C" using f-string

print("Practice formatting strings ✍️")

