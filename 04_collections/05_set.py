"""
--------------------------------------------------
SETS IN PYTHON
--------------------------------------------------

Set = {}

Properties:
- Unordered (no indexing)
- Mutable (can add/remove items)
- No duplicate values
- Fast membership checking

Important:
Elements inside a set must be immutable
(strings, numbers, tuples are allowed)
"""


# --------------------------------------------------
# Creating a Set
# --------------------------------------------------

fruits = {"apple", "orange", "grape", "banana"}

print("\nOriginal set:")
print(fruits)   # Note: Order may change every run 


# --------------------------------------------------
# Indexing is NOT allowed
# --------------------------------------------------

# print(fruits[0])  # ❌ Error: sets are unordered


# --------------------------------------------------
# Adding Items
# --------------------------------------------------

fruits.add("pineapple")
print("\nAfter add('pineapple'):")
print(fruits)


# --------------------------------------------------
# Removing Items
# --------------------------------------------------

# remove(value) → gives error if value not found
fruits.remove("apple")
print("\nAfter remove('apple'):")
print(fruits)

# pop() → removes a random element
removed_item = fruits.pop()
print("\nRemoved using pop():", removed_item)
print("Set now:", fruits)


# --------------------------------------------------
# Duplicate Values Not Allowed
# --------------------------------------------------

animals = {"cat", "dog", "cat", "tiger", "deer"}

print("\nAnimals set (duplicates removed automatically):")
print(animals)


# --------------------------------------------------
# Membership Check (Very Fast in Sets)
# --------------------------------------------------

print("\nMembership check:")
print("Is 'dog' in animals?", "dog" in animals)
print("Is 'lion' in animals?", "lion" in animals)


# --------------------------------------------------
# Length
# --------------------------------------------------

print("\nNumber of animals:", len(animals))


# --------------------------------------------------
# Set Operations (Important Feature)
# --------------------------------------------------

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("\nSet 1:", set1)
print("Set 2:", set2)

# Union → combine both sets
print("Union:", set1.union(set2))

# Intersection → common values
print("Intersection:", set1.intersection(set2))

# Difference → values in set1 not in set2
print("Difference (set1 - set2):", set1.difference(set2))


# --------------------------------------------------
# Clearing a Set
# --------------------------------------------------

fruits.clear()
print("\nAfter clear():")
print(fruits)


# --------------------------------------------------
# Empty Set Initialization
# --------------------------------------------------

# {} creates empty dictionary, NOT set correct way is below
cars = set()

print("\nEmpty set created:")
print(cars)