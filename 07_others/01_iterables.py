"""
--------------------------------------------------
ITERABLE IN PYTHON - SIMPLE EXAMPLE
--------------------------------------------------

Iterable = An object that can be looped over.

Common iterables:
- list
- tuple
- string
- dictionary
- set
"""

# --------------------------------------------------
# 1️⃣ List (Iterable)
# --------------------------------------------------

numbers = [1, 2, 3, 4]

print("List Example:")
for num in numbers:
    print(num)


# --------------------------------------------------
# 2️⃣ String (Iterable)
# --------------------------------------------------

name = "Arun"

print("\nString Example:")
for char in name:
    print(char)


# --------------------------------------------------
# 3️⃣ Tuple (Iterable)
# --------------------------------------------------

colors = ("red", "green", "blue")

print("\nTuple Example:")
for color in colors:
    print(color)


# --------------------------------------------------
# 4️⃣ Dictionary (Iterable)
# --------------------------------------------------

person = {
    "name": "Arun",
    "age": 25,
    "city": "Kannur"
}

print("\nDictionary Example (Keys):")
for key in person:
    print(key)


print("\nDictionary Example (Values):")
for value in person.values():
    print(value)


print("\nDictionary Example (Key and Value):")
for key, value in person.items():
    print(f"{key}: {value}")


# --------------------------------------------------
# 5️⃣ Set (Iterable)
# --------------------------------------------------

fruits = {"apple", "banana", "orange"}

print("\nSet Example:")
for fruit in fruits:
    print(fruit)


# --------------------------------------------------
# 6️⃣ Check if Object is Iterable
# --------------------------------------------------

from collections.abc import Iterable

print("\nChecking Iterable:")

print("Is numbers iterable?", isinstance(numbers, Iterable))
print("Is name iterable?", isinstance(name, Iterable))
print("Is 100 iterable?", isinstance(100, Iterable))  # False