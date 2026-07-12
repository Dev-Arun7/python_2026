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


# Learn more below if you're interest to know more...


# ==================================================
# ADDITIONAL TRY-EXCEPT CONCEPTS
# ==================================================

# --------------------------------------------------
# Example 4: Catching a specific exception
# --------------------------------------------------
print("\nExample 4: Catching a specific exception")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("❌ Please enter numbers only!")

# Explanation:
# It is better to catch the specific exception that you expect.
# Here, int() raises ValueError if the input is not a valid number.
# Avoid using a bare 'except:' unless absolutely necessary.


# --------------------------------------------------
# Example 5: Using else
# --------------------------------------------------
print("\nExample 5: Using else")

try:
    num = int(input("Enter a number: "))
except ValueError:
    print("❌ Invalid number!")
else:
    print("✅ Conversion successful!")
    print("Number is:", num)

# Explanation:
# The else block runs ONLY if the try block succeeds.
# If an exception occurs, else is skipped.


# --------------------------------------------------
# Example 6: Using finally
# --------------------------------------------------
print("\nExample 6: Using finally")

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("❌ Invalid number!")
finally:
    print("🔹 This always runs.")

# Explanation:
# The finally block always runs whether an exception happens or not.
# It is commonly used for cleaning up resources like closing files,
# database connections, or network connections.


# --------------------------------------------------
# Example 7: Getting the actual error message
# --------------------------------------------------
print("\nExample 7: Printing the error message")

try:
    num = int(input("Enter a number: "))
except ValueError as error:
    print("❌ Error:", error)

# Explanation:
# "as error" stores the exception object in the variable 'error'.
# Printing it shows Python's actual error message.
# This is very useful while debugging.


# --------------------------------------------------
# Example 8: Catching multiple exceptions together
# --------------------------------------------------
print("\nExample 8: Catching multiple exceptions together")

try:
    value = input("Enter a number: ")
    num = int(value)

    result = "Hello" + num
    print(result)

except (ValueError, TypeError):
    print("❌ ValueError or TypeError occurred.")

# Explanation:
# Multiple exceptions can be grouped together using parentheses.
# This is useful when different exceptions should be handled the same way.


# --------------------------------------------------
# Example 9: Raising your own exception
# --------------------------------------------------
print("\nExample 9: Raising your own exception")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as error:
    print("❌", error)

# Explanation:
# The raise keyword allows you to create your own exception.
# This is commonly used when validating user input or program data.


# --------------------------------------------------
# Example 10: Order of except blocks
# --------------------------------------------------
print("\nExample 10: Order of except blocks")

try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)

except ValueError:
    print("❌ Please enter numbers only.")

except ZeroDivisionError:
    print("❌ Cannot divide by zero.")

except Exception as error:
    print("❌ Some other error occurred:", error)

# Explanation:
# Python checks except blocks from top to bottom.
# Always place specific exceptions first.
# Keep the general Exception block last.


# --------------------------------------------------
# Summary
# --------------------------------------------------
print("\n==================== SUMMARY ====================")
print("try      -> Code that might cause an exception.")
print("except   -> Runs only if an exception occurs.")
print("else     -> Runs only if no exception occurs.")
print("finally  -> Always runs.")
print("raise    -> Create your own exception.")
print("=================================================")

# ==================================================
# Good Practices
# ==================================================
#
# ✅ Catch specific exceptions whenever possible.
#
# Good:
#     except ValueError:
#
# Better:
#     except ValueError as error:
#
# Less recommended:
#     except Exception:
#
# Avoid:
#     except:
#
# Reason:
# A bare 'except:' catches every exception, even ones like
# KeyboardInterrupt (Ctrl + C) and SystemExit, making debugging harder.
#
# ==================================================