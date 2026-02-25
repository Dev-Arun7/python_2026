"""
--------------------------------------------------
LISTS (BASICS)
--------------------------------------------------

Collection = A single variable that stores multiple values.

Main collection types:
1) List       []  ordered, changeable (mutable), allows duplicates
2) Tuple      ()  ordered, NOT changeable (immutable), allows duplicates
3) Set        {}  unordered, changeable, NO duplicates
4) Dictionary {}  key-value pairs, keys are unique

In this file, we focus on LIST BASICS:
- Creating a list
- Indexing
- Slicing
- Looping
"""

# --------------------------------------------------
# Why lists?
# --------------------------------------------------

# Without a list, you might do this:
fruit_1 = "apple"
fruit_2 = "mango"
fruit_3 = "orange"

print("\nWithout list:")
print(fruit_1, fruit_2, fruit_3)

# With a list:  one variable store all values
fruits = ["apple", "mango", "orange", "grape", "banana"]

print("\nWith list:")
print(fruits)  # prints all values


# --------------------------------------------------
# Indexing (start from 0)
# --------------------------------------------------
# Printing individual values just like without list
print("\nIndexing:")
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])
print("Last fruit:", fruits[-1])  # negative index gives from the end


# --------------------------------------------------
# Slicing
# slice format: list[start:stop:step]
# stop is NOT included
# --------------------------------------------------

print("\nSlicing:")
print("First 3 fruits:", fruits[0:3])   # apple, mango, orange
print("All fruits:", fruits[:])         # full list copy-like display
print("Every 2nd fruit:", fruits[::2])  # step of 2
print("Reverse list:", fruits[::-1])    # reverse using slicing


# --------------------------------------------------
# Looping through a list
# --------------------------------------------------

print("\nLoop through all fruits:")
for fruit in fruits:
    print(fruit)

print("\nFind a particular value:")
for fruit in fruits:
    if fruit == "mango":
        print("Found:", fruit)


# --------------------------------------------------
# Membership check (best way to check existence)
# --------------------------------------------------

print("\nMembership check:")
value = "apple" in fruits
print("Is 'apple' in fruits?", value)

print("Is 'kiwi' in fruits?", "kiwi" in fruits)


# --------------------------------------------------
# Length of list
# --------------------------------------------------

print("\nLength of list:")
print("Total fruits:", len(fruits))



# Initilize empty list
cars = [] # Create a new list variable with no values in it

