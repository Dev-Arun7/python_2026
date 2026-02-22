"""
--------------------------------------------------
LISTS (COMMON METHODS)
--------------------------------------------------

This file focuses on common list methods:
- append, insert, extend
- pop, remove, clear
- index, count
- sort, reverse
- copy

Important:
Some methods MODIFY the original list in-place.
So we often use a fresh list for each example.
"""


def print_state(title: str, items: list[str]) -> None:
    """Helper function to print list neatly."""
    print(f"{title}: {items}")


# --------------------------------------------------
# Starting list
# --------------------------------------------------

fruits = ["apple", "mango", "orange", "grape", "banana"]
print_state("\nOriginal", fruits)


# --------------------------------------------------
# Add items
# --------------------------------------------------

# append() → add at the end
fruits.append("kiwi")
print_state("After append('kiwi')", fruits)

# insert(index, value) → add at a specific position
fruits.insert(2, "strawberry")
print_state("After insert(2, 'strawberry')", fruits)

# extend(list) → add multiple items
more_fruits = ["papaya", "watermelon"]
fruits.extend(more_fruits)
print_state("After extend([...])", fruits)


# --------------------------------------------------
# Remove items
# --------------------------------------------------

# pop() → removes and returns last item (or item at index)
last_item = fruits.pop()
print("\nRemoved using pop():", last_item)
print_state("After pop()", fruits)

second_item = fruits.pop(1)
print("Removed using pop(1):", second_item)
print_state("After pop(1)", fruits)

# remove(value) → removes first matching value
# If the value is not present, it throws ValueError
if "mango" in fruits:
    fruits.remove("mango")
print_state("After remove('mango')", fruits)


# --------------------------------------------------
# Find information
# --------------------------------------------------

# index(value) → returns index of first match (ValueError if not found)
if "banana" in fruits:
    print("\nIndex of 'banana':", fruits.index("banana"))
else:
    print("\n'banana' not found, cannot use index() safely")

# count(value) → how many times a value appears
# NOTE: your earlier code had "banana " (with a space) which would not match "banana"
print("Count of 'apple':", fruits.count("apple"))


# --------------------------------------------------
# Sorting and reversing
# --------------------------------------------------

# sort() sorts the list in-place
fruits.sort()
print_state("\nAfter sort()", fruits)

# reverse() reverses in-place
fruits.reverse()
print_state("After reverse()", fruits)


# --------------------------------------------------
# Copying
# --------------------------------------------------

# copy() creates a new list (shallow copy)
fruits_copy = fruits.copy()
print_state("\nCopy created", fruits_copy)

# Modifying copy does not change original
fruits_copy.append("dragonfruit")
print_state("After modifying copy", fruits_copy)
print_state("Original remains", fruits)


# --------------------------------------------------
# Clear the list
# --------------------------------------------------

fruits.clear()
print_state("\nAfter clear()", fruits)