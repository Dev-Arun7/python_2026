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

# With a list:
fruits = ["apple", "mango", "orange", "grape", "banana"]

print("\nWith list:")
print(fruits)  # prints all values


# --------------------------------------------------
# Indexing (start from 0)
# --------------------------------------------------

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
















"""
Collection = A single variable to store multiple similar values
There are many types
1.List = [] orderd, changable, duplicates 
2.set = {} 
3. Tuple = ()
4. Dictionary = {}
Here we focus on list which stores differet values ..... 
"""
 
# I need to store different fruit names on variables
fruit_1 = "apple"
fruit_2 = "mango"
fruit_3 = "orange"


# Instead of this i can use a single variable
fruits = ["apple", "mango", "orange", "grape", "banana"]
print(fruits) # print all values

# print first fruit
print(fruits[0])

# Print second fruits
print(fruits[1])

# print(fruits[4]) # Error

# printing using slicing
print(fruits[0: 3])

# Print all
print(fruits[:])

# print all with step 2
print(fruits[::2])

# print reverse order
print(fruits[::-1])

# print all fruits using for loop
for fruit in fruits:
    print(fruit)


# Check and print a particular value
for fruit in fruits:
    if fruit == "mango":
        print(fruit) 



# Show all the functions available on a collection
print(dir(fruits))

# Help
print(help(fruits))

# --------  COMMON FUNCTIONS  USING ON LIST ------------
# Find length
print(len(fruits))

# Check value in  list
value = "apple" in fruits
print(value)  # print True if apple in list


# Sort


# copy

# Add a value at last

# remove value from last

# add value at first

# take the first value 

# remove an element
fruits.remove("mango")

# insert a value at an index
fruits.insert(2, "strawberry")

# Reverse
fruits.reverse()

# Clear 
fruits.clear() 

# Find index
print(fruits.index("banana"))

# count 
print(fruits.count("banana "))

# change value in first postion
fruits[0] = "blueberry" 

