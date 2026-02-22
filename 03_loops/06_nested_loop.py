"""
--------------------------------------------------
NESTED LOOPS IN PYTHON
--------------------------------------------------

A nested loop means:
    A loop inside another loop.

Structure:

Outer Loop
    └── Inner Loop

For every ONE iteration of the outer loop,
the inner loop runs completely.

Both loops can be:
- for loop
- while loop
"""

# --------------------------------------------------
# Example 1: Print a name multiple times (character by character)
# --------------------------------------------------

print("\nExample 1: Print characters in multiple rows\n")

name = "Arun Balakrishnan"
rows = 3

for row in range(rows):          # Outer loop → controls rows
    for letter in name:          # Inner loop → runs fully each row
        print(letter, end=" ")   # Print in same line
    print()                      # Move to next line after inner loop


# --------------------------------------------------
# Example 2: Print a rectangle pattern
# --------------------------------------------------

print("\nExample 2: Rectangle Pattern\n")

symbol = input("Enter the symbol: ")
rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

for row in range(rows):
    for col in range(columns):
        print(symbol, end=" ")
    print()


# --------------------------------------------------
# Example 3: Print a right-angled triangle
# --------------------------------------------------

print("\nExample 3: Right-Angled Triangle\n")

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()


# --------------------------------------------------
# Example 4: Print numbers pattern
# --------------------------------------------------

print("\nExample 4: Number Pattern\n")

rows = 5

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


# --------------------------------------------------
# Example 5: Multiplication Table (1 to 5)
# --------------------------------------------------

print("\nExample 5: Multiplication Table (1 to 5)\n")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")   # formatted spacing
    print()