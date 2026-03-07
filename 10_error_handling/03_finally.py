"""
What is finally?

The finally block ALWAYS runs.

It does not matter:
- If error happens
- If no error happens
- Even if we use return inside function

finally is usually used for:
- Closing files
- Cleaning resources
- Printing final message
"""

# ---------------------------------------------------
# Example 1: finally without error

print("Example 1: No Error Case")

try:
    # Normal division (no error)
    number = 10
    result = number / 2
    print("Result:", result)

except ZeroDivisionError:
    # This will NOT run because there is no error
    print("Cannot divide by zero!")

finally:
    # This ALWAYS runs
    print("This always runs (Example 1).")

print("Program continues...\n")


# ---------------------------------------------------
# Example 2: finally with error

print("Example 2: Error Case")

try:
    number = 10
    result = number / 0   # This causes ZeroDivisionError
    print("Result:", result)

except ZeroDivisionError:
    # This runs because error happened
    print("Cannot divide by zero!")

finally:
    # Even though error happened,
    # finally block still runs
    print("This always runs (Example 2).")

print("Program continues...\n")


# ---------------------------------------------------
# Example 3: finally inside a function

print("Example 3: finally inside function")

def divide_numbers(a, b):
    try:
        # Try to divide numbers
        result = a / b
        print("Result:", result)

    except ZeroDivisionError:
        # Handles division by zero
        print("Cannot divide by zero!")

    finally:
        # This always executes
        print("Division attempt completed.\n")


# Calling function with valid input
divide_numbers(20, 4)

# Calling function with invalid input (division by zero)
divide_numbers(10, 0)


# ---------------------------------------------------
# Example 4: finally inside loop

print("Example 4: finally inside loop")

while True:
    user_input = input("Enter a number to divide 100 (or type 'exit'): ")

    # Exit condition
    if user_input == "exit":
        print("Exiting loop...")
        break

    try:
        # Convert input to integer
        number = int(user_input)

        # Try division
        result = 100 / number
        print("Result:", result)

    except ValueError:
        # If user enters text
        print("Invalid input!")

    except ZeroDivisionError:
        # If user enters 0
        print("Cannot divide by zero!")

    finally:
        # This runs every time,
        # whether error happens or not
        print("Attempt finished.\n")

print("Program finished successfully 😊")