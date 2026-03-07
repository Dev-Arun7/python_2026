"""
Why do we need error handling?

Sometimes our program crashes because of errors.
Example:
- Dividing by zero
- Converting text to number
- Taking input wrongly

If we don’t handle errors, the program will stop immediately.

Using try and except helps us:
1. Prevent program crash
2. Show user-friendly message
3. Continue running the program
"""

# ---------------------------------------------------
# Example 1: Basic try-except

print("Example 1: Basic Division")

try:
    number = 10
    result = number / 2
    print("Result:", result)

except:
    # This block runs only if error happens
    print("Something went wrong!")

# Try 0 instead of 2, the result won't show up but still rest of the code continues
# try this without as well in another script what will happen if there's not try-except

print("Program continues...\n")


# ---------------------------------------------------
# Example 2: Handling division by zero

print("Example 2: Division by Zero")

try:
    number = 10
    result = number / 0   # This will cause error
    print("Result:", result)

except ZeroDivisionError:
    # This block runs only for division by zero error
    print("You cannot divide by zero!")

print("Program continues...\n")

# ---------------------------------------------------
# Example 3: Handling user input error

print("Example 3: Converting input to integer")

try:
    user_input = input("Enter a number: ")
    number = int(user_input)   # Error if user types text
    print("You entered:", number)

except ValueError:
    print("Invalid input! Please enter a valid number.")

print("Program continues...\n")


# ---------------------------------------------------
# Example 4: Using else block

"""
else block runs only if NO error occurs
"""

print("Example 4: try-except-else")

try:
    number = 20
    result = number / 4
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful. Result:", result)

print("Program continues...\n")

# ---------------------------------------------------
# Example 5: Using try-except inside a loop

print("Example 6: Loop with error handling")

while True:
    user_input = input("Enter a number to divide 100 (or type 'exit'): ")

    if user_input == "exit":
        print("Exiting loop...")
        break

    try:
        number = int(user_input)
        result = 100 / number
        print("Result:", result)

    except ZeroDivisionError:
        print("Cannot divide by zero!")

    except ValueError:
        print("Please enter a valid number!")

print("Program finished successfully 😊")



"""
Try your own by providing the value which causes error
also try these code without try-except on new file to see what will happen
"""