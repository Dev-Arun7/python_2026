"""
What is Multiple Exception Handling?

Sometimes a single block of code can produce
different types of errors.

Instead of writing separate try-except blocks,
we can handle multiple errors inside one try block.

This makes the code clean and readable.
"""

# ---------------------------------------------------
# Example 1: Multiple except blocks

print("Example 1: Handling Different Errors")

try:
    user_input = input("Enter a number: ")
    number = int(user_input)      # May cause ValueError
    result = 100 / number         # May cause ZeroDivisionError
    print("Result:", result)

except ValueError:
    print("Error: You must enter a valid number!")

except ZeroDivisionError:
    print("Error: You cannot divide by zero!")

print("Program continues...\n")


# ---------------------------------------------------
# Example 2: Handling multiple exceptions in one line

"""
We can also handle multiple errors together
using a tuple.
"""

print("Example 2: Multiple errors in single except")

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 50 / number
    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Something went wrong! Check your input.")

print("Program continues...\n")


# ---------------------------------------------------
# Example 3: Showing the actual error message

"""
We can capture the error inside a variable
using 'as'
"""

print("Example 3: Capturing error message")

try:
    user_input = input("Enter a number: ")
    number = int(user_input)
    result = 10 / number
    print("Result:", result)

except (ValueError, ZeroDivisionError) as error:
    print("An error occurred:")
    print("Error message:", error)

print("Program finished successfully 😊")