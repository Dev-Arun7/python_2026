"""
--------------------------------------------------
2D LISTS (LIST INSIDE A LIST) IN PYTHON
--------------------------------------------------

A 2D list means: a list that contains other lists.

Think of it like:
- Rows and Columns (like a table)
- Matrix style data (like Excel sheet)

Example:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

Written in a cleaner format:

matrix = [
    [1, 2, 3],   # Row 0
    [4, 5, 6],   # Row 1
    [7, 8, 9]    # Row 2
]

Important:
matrix[row][column]

To work with 2D lists, we often use NESTED LOOPS.
Outer loop → rows
Inner loop → columns
"""

# --------------------------------------------------
# Example 1: Basic 2D List (Matrix)
# --------------------------------------------------

print("\nExample 1: Basic 2D List (Matrix)\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
print(matrix)

# Each item in matrix is actually a LIST
print("\nPrint each row:")
for row in matrix:
    # 'row' itself is a list
    print(row)

print("\nPrint each value (using nested loop):")

# Outer loop → picks one row at a time
for row in matrix:
    # Inner loop → goes through each value inside that row
    for value in row:
        print(value, end=" ")
    # Move to next line after finishing one row
    print()


# --------------------------------------------------
# Example 2: Accessing elements using index
# --------------------------------------------------

print("\nExample 2: Accessing elements using index\n")

# matrix[row_index][column_index]

print("First row:", matrix[0])             # Entire first row
print("First value of first row:", matrix[0][0])
print("Last value of last row:", matrix[-1][-1])

print("\nPrint all elements using index:")

# len(matrix) → number of rows
for row_index in range(len(matrix)):
    # len(matrix[row_index]) → number of columns in that row
    for col_index in range(len(matrix[row_index])):
        print(matrix[row_index][col_index], end=" ")
    print() # Next line after finish inner loop


# --------------------------------------------------
# Example 3: 2D List of Fruits
# --------------------------------------------------

print("\nExample 3: 2D List of Fruits\n")

fruit_groups = [
    ["apple", "mango", "banana"],
    ["grape", "orange"],
    ["kiwi", "papaya", "watermelon"]
]

print("Fruit Groups:")
for group in fruit_groups:
    # Each group is a separate list
    print(group)

print("\nPrint each fruit one by one:")

for group in fruit_groups:      # Outer loop → each sublist
    for fruit in group:         # Inner loop → each item in sublist
        print(fruit, end="  ")
    print()


# --------------------------------------------------
# Example 4: Update a value in a 2D List
# --------------------------------------------------

print("\nExample 4: Update a value in 2D List\n")

print("Before update:", matrix)

# Change value at row 1, column 1
# (Row 1 = [4, 5, 6], Column 1 = 5)
matrix[1][1] = 99

print("After update:", matrix)


# --------------------------------------------------
# Example 5: Create a 2D List using loops (simple table)
# --------------------------------------------------

print("\nExample 5: Create a 2D List using loops\n")

rows = 3
cols = 4
table = []

# We create rows one by one
for r in range(rows):

    row = []  # Create an empty list for each row

    # Add values to this row
    for c in range(cols):
        row.append(0)   # Add 0 for each column

    # Add completed row to table
    table.append(row)

print("Generated Table (3x4 filled with 0):")
for row in table:
    print(row)


# --------------------------------------------------
# Example 6: Mini Practice - Total of each row
# --------------------------------------------------

print("\nExample 6: Total of each row\n")

numbers = [
    [10, 20, 30],
    [5,  5,  5],
    [1,  2,  3]
]

# Outer loop → goes row by row
for row in numbers:

    total = 0  # Reset total for each row

    # Inner loop → adds each number inside that row
    for value in row:
        total += value

    print("Row:", row, "→ Total:", total)


# --------------------------------------------------
# Example: Create a 2D List with column index values
# --------------------------------------------------

print("\nExample: Table with column numbers\n")

rows = 3
cols = 4
table = []

# Create rows one by one
for r in range(rows):

    row = []  # Create empty list for each row

    # Add column index values
    for c in range(cols):
        row.append(c)   # Add column number (0,1,2,3)

    # Add completed row to table
    table.append(row)

print("Generated Table:")
for row in table:
    print(row)

# --------------------------------------------------
# Example: Create a pattern table (123, 456, 789)
# --------------------------------------------------

print("\nExample: Pattern table\n")

rows = 3
cols = 3
table = []

num = 1  # Starting number

# Create rows one by one
for r in range(rows):

    row = []  # Empty row

    # Add increasing numbers
    for c in range(cols):
        row.append(num)  # Add current number
        num += 1         # Increase number

    # Add row to table
    table.append(row)

print("Generated Table:")
for row in table:
    print(row)


"""
SUMMARY:

1D List:
    [1, 2, 3]

2D List:
    [
        [1, 2, 3],
        [4, 5, 6]
    ]

Access format:
    list[row][column]

Outer loop  → rows
Inner loop  → columns
"""