"""
--------------------------------------------------
TRY-EXCEPT FOR BEGINNERS
--------------------------------------------------

Introduction:
- Sometimes our program can crash if the user gives wrong input.
- Example: dividing by zero, typing letters instead of numbers.
- We use try-except to "catch" errors and prevent the crash.
- "try" → the code that might fail
- "except" → what to do if it fails
--------------------------------------------------
"""

# -------------------------------
# Example 1: Entering a number
# -------------------------------
print("Example 1: Enter a number")
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except:
    print("❌ That is not a valid number!")

# Explanation:
# If the user types letters or symbols instead of a number,
# normally the program would crash with ValueError.
# By putting the code in try-except, the program does not crash.
# The except block runs instead and shows a friendly message.


# -------------------------------
# Example 2: Division
# -------------------------------
print("\nExample 2: Division")
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result of division:", result)
except ZeroDivisionError:
    print("❌ You cannot divide by zero!")
except:
    print("❌ Please enter valid numbers!")

# Explanation:
# Division by zero will normally crash the program.
# Also, typing letters instead of numbers would crash.
# Using try-except, we catch both errors separately and show friendly messages.


# -------------------------------
# Example 3: Accessing a list element
# -------------------------------
print("\nExample 3: Picking from a list")
fruits = ["apple", "banana", "orange"]
print("Fruits list:", fruits)

try:
    index = int(input("Enter index of fruit (0-2): "))
    print("You picked:", fruits[index])
except IndexError:
    print("❌ That index does not exist! Choose 0, 1, or 2.")
except:
    print("❌ Please enter a valid number!")

# Explanation:
# If the user types a number outside the list range, normally IndexError occurs.
# If user types a letter instead of number, ValueError occurs.
# Using try-except, program continues safely and shows friendly messages.


# -------------------------------
# End of Practice
# -------------------------------
print("\n✅ You have learned the basics of try-except!")
print("Try typing wrong inputs to see how errors are handled safely.")