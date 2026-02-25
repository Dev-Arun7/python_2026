"""
--------------------------------------------------
LISTS (COMMON METHODS)
--------------------------------------------------

This file explains common list methods:

append()   → Add value at end
insert()   → Add value at specific index
extend()   → Add multiple values
pop()      → Remove last (or specific index)
remove()   → Remove by value
index()    → Find position of value
count()    → Count occurrences
sort()     → Sort list
reverse()  → Reverse list
copy()     → Create copy
clear()    → Remove all items

Important:
Most list methods MODIFY the original list.
"""

# --------------------------------------------------
# Starting List
# --------------------------------------------------

fruits = ["apple", "mango", "orange", "grape", "banana"]

print("\nOriginal list:")
print(fruits)


# --------------------------------------------------
# ADDING ITEMS
# --------------------------------------------------

# append() → add at end
fruits.append("kiwi")
print("\nAfter append('kiwi'):")
print(fruits)

# insert(index, value)
fruits.insert(2, "strawberry")
print("\nAfter insert(2, 'strawberry'):")
print(fruits)

# extend() → add multiple values
more_fruits = ["papaya", "watermelon"]
fruits.extend(more_fruits)
print("\nAfter extend([...]):")
print(fruits)


# --------------------------------------------------
# REMOVING ITEMS
# --------------------------------------------------

# pop() → removes last item
removed_item = fruits.pop()
print("\nRemoved using pop():", removed_item)
print("List now:", fruits)

# pop(index) removing value in first (1) index
removed_item = fruits.pop(1)
print("\nRemoved using pop(1):", removed_item)
print("List now:", fruits)

# remove(value)
if "mango" in fruits:
    fruits.remove("mango")

print("\nAfter remove('mango'):")
print(fruits)


# --------------------------------------------------
# FINDING INFORMATION
# --------------------------------------------------

# index(value)
if "banana" in fruits:
    print("\nIndex of 'banana':", fruits.index("banana"))
else:
    print("\nBanana not found")

# count(value)
print("Count of 'apple':", fruits.count("apple"))


# --------------------------------------------------
# SORTING & REVERSING
# --------------------------------------------------

fruits.sort()
print("\nAfter sort():")
print(fruits)

fruits.reverse()
print("\nAfter reverse():")
print(fruits)


# --------------------------------------------------
# COPYING
# --------------------------------------------------

fruits_copy = fruits.copy()
print("\nCopied list:")
print(fruits_copy)

fruits_copy.append("dragonfruit")

print("\nAfter modifying copy:")
print("Copy:", fruits_copy)
print("Original:", fruits)


# --------------------------------------------------
# CLEAR LIST
# --------------------------------------------------

fruits.clear()
print("\nAfter clear():")
print(fruits)