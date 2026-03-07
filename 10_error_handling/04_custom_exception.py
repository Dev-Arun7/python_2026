"""
------------------------------------------------------------------------
Note: This is a bit advanced topic. You may not need to learn this now
until you're super curious 😊
------------------------------------------------------------------------

What is a Custom Exception?

Python already has many built-in errors like:
- ValueError
- ZeroDivisionError
- TypeError

But sometimes we want to create our own error
for our own rules.

This is called a Custom Exception.
"""

# ---------------------------------------------------
# Step 1: Creating a Custom Exception

# To create a custom exception,
# we create a class that inherits from Exception

class AgeTooSmallError(Exception):
    # We don't need to write anything inside for now
    pass


# ---------------------------------------------------
# Example 1: Using Custom Exception

print("Example 1: Age Check")

def check_age(age):
    # If age is less than 18, raise our custom error
    if age < 18:
        raise AgeTooSmallError("Age must be 18 or above.")
    
    print("Access granted!")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)

except AgeTooSmallError as error:
    # This catches our custom error
    print("Custom Error:", error)

except ValueError:
    # This catches wrong input (like text)
    print("Please enter a valid number.")

print("Program continues...\n")


# ---------------------------------------------------
# Example 2: Custom Exception for Bank Balance

print("Example 2: Bank Withdrawal")

class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):
    # If withdrawal amount is greater than balance
    if amount > balance:
        raise InsufficientBalanceError("Not enough balance.")
    
    balance = balance - amount
    print("Withdrawal successful.")
    print("Remaining balance:", balance)


try:
    account_balance = 5000
    withdraw_amount = int(input("Enter withdrawal amount: "))
    
    withdraw(account_balance, withdraw_amount)

except InsufficientBalanceError as error:
    print("Custom Error:", error)

except ValueError:
    print("Please enter a valid number.")

print("Program finished successfully 😊")