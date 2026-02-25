"""
--------------------------------------------------
2D LISTS IN PYTHON — CLEAN VERSION
--------------------------------------------------

A 2D list is a list of lists.
Each inner list is like a row in a table.
"""

# --------------------------------------------------
# Create normal lists
# --------------------------------------------------

fruits = ["apple", "banana", "cherry"]
vegetables = ["carrot", "broccoli", "spinach"]
meats = ["chicken", "beef", "pork"]

# Create a 2D list using existing lists
groceries = [fruits, vegetables, meats]

print("Full 2D list:")
print(groceries)

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# Access inner lists
# --------------------------------------------------

print("Fruits list:", groceries[0])
print("Vegetables list:", groceries[1])
print("Meats list:", groceries[2])

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# Access individual items using two indices
# --------------------------------------------------

print("Second fruit:", groceries[0][1])   # banana
print("First vegetable:", groceries[1][0])  # carrot 
print("Third meat:", groceries[2][2])    # pork

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# Create 2D list directly
# --------------------------------------------------

groceries_2 = [
    ["apple", "banana", "cherry"],       # fruits
    ["carrot", "broccoli", "spinach"],   # vegetables
    ["chicken", "beef", "pork"]          # meats
]

print("Directly created 2D list:")
print(groceries_2)

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# Loop through each inner list
# --------------------------------------------------

print("Printing each category:")

for category in groceries_2:
    print(category)

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# Loop through each item
# --------------------------------------------------

print("Printing each item:")

for category in groceries_2:
    for item in category:
        print(item, end=" ")
    print()

print("\n--------------------------------------------------\n")

# --------------------------------------------------
# 2D collection with different data types
# --------------------------------------------------

data = [
    ("cat", "dog", "rabbit"),            # tuple
    ["red", "green", "blue", "black"],   # list (different length)
    {"london", "paris", "new york"}      # set (unordered)
]

print("Mixed 2D collection:")
print(data)

print("\nNote: Sets do NOT maintain order.\n")

# Loop through mixed data
for group in data:
    print(group)