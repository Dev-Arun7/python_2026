"""
--------------------------------------------------
TUPLES — INTERMEDIATE
--------------------------------------------------
"""

# --------------------------------------------------
# Packing
# --------------------------------------------------

colors = "red", "green", "blue"  # This is a tuple (even though you didn't add any parathesis)
                                 # Python does it for you.

print("\nTuple packing:")
print(colors)


# --------------------------------------------------
# Unpacking
# --------------------------------------------------

a, b, c = colors   # items inside the colors asigns automatically, respectively

print("\nUnpacked values:")
print(a, b, c)

# This is very similar to accessing by index, but more readable and 
# convenient when you have many values.
# For example:
x = colors[0]
y = colors[1]
z = colors[2] # same as a, b, c = colors but more verbose


# Unpacking automatically assigns tuple values to variables
# It is similar to accessing by index, but cleaner and shorter

# Instead of:
# x = colors[0]
# y = colors[1]
# z = colors[2]

# We can simply write:
# a, b, c = colors

# --------------------------------------------------
# Count Method
# --------------------------------------------------

numbers = (1, 2, 2, 3, 4, 4, 4)

print("\nCount of 4:", numbers.count(4))


# --------------------------------------------------
# Index Method
# --------------------------------------------------

print("Index of 3:", numbers.index(3))


# --------------------------------------------------
# Convert Tuple to List to Modify
# --------------------------------------------------

fruits = ("apple", "orange", "grape")

temp = list(fruits)
temp[0] = "mango"
fruits_modified = tuple(temp)

print("\nModified tuple:")
print(fruits_modified)


# --------------------------------------------------
# Concatenation
# --------------------------------------------------

tuple1 = (1, 2, 3)
tuple2 = (4, 5)

combined = tuple1 + tuple2

print("\nCombined tuple:")
print(combined)


# --------------------------------------------------
# Repetition
# --------------------------------------------------

repeat = ("hi",) * 3

print("\nRepeated tuple:")
print(repeat)


# --------------------------------------------------
# Nested Tuple
# --------------------------------------------------

nested = ((1, 2), (3, 4))

print("\nNested tuple:")
print(nested)


# --------------------------------------------------
# Practice Problems
# --------------------------------------------------

nums = (10, 20, 30, 40)

# Sum
total = 0
for n in nums:
    total += n

print("\nSum:", total)


# Max value
max_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n

print("Max:", max_val)


# Reverse print
print("\nReverse:")

for i in range(len(nums)-1, -1, -1):
    print(nums[i])


# --------------------------------------------------
# Real Example
# --------------------------------------------------

students = (
    ("Arun", 85),
    ("Rahul", 90),
    ("Anila", 88)
)

print("\nStudents marks:")

for s in students:
    print(s[0], "scored", s[1])