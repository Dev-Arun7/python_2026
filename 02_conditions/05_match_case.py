# Match case statements
# A match case statement is used to compare a value against multiple patterns.
# It works similar to switch-case in other languages.
# Note: Match case statements were introduced in Python 3.10, so make sure to use Python 3.10 or later to run this code.

# --------------------------------------------------
# Example 1: Simple Day Checker
# --------------------------------------------------

day = "Monday"

match day:
    case "Monday":
        print("Start of the work week!")
    case "Friday":
        print("Weekend is coming soon!")
    case "Saturday":
        print("It's the weekend!")
    case "Sunday":
        print("It's the weekend!")
    case _:  # default case (like else)
        print("Just a normal day")


# --------------------------------------------------
# Example 2: Grade Checker
# --------------------------------------------------

grade = "B"

match grade:
    case "A":
        print("Excellent work!")
    case "B":
        print("Good job!")
    case "C":
        print("You passed!")
    case "D":
        print("You need improvement!")
    case _:
        print("Invalid grade")


# --------------------------------------------------
# Example 3: Login Role Check
# --------------------------------------------------

role = "admin"

match role:
    case "admin":
        print("Welcome, admin! You have full access.")
    case "editor":
        print("Welcome, editor! You can edit content.")
    case "viewer":
        print("Welcome, viewer! You can view content.")
    case _:
        print("Invalid role")

# --------------------------------------------------
# Example 4: ATM Withdrawal Check
# --------------------------------------------------

action = "withdraw"
balance = 1000

match action:
    # case balance checking
    case "check_balance":
        print("Your balance is:", balance)
    # case withdrawal
    case "withdraw":
        if balance >= 500:
            print("Withdrawal successful!")
        else:
            print("Insufficient funds!")
    # Case deposit
    case "deposit":
        print("Deposit successful!")
    # default case
    case _:
        print("Invalid action")


