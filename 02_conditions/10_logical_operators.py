# Logical Operators
# Logical operators are used to combine multiple conditions.

# There are 3 logical operators:
# and → True if BOTH conditions are true
# or  → True if ANY condition is true
# not → Reverses the result



# --------------------------------------------------
# Example 1: AND Operator
# --------------------------------------------------

age = 25
has_id = True

if age >=18 and has_id: 
    print("You can enter the club...")
else:
    print("Entry denied...!")


# --------------------------------------------------
# Example 2: OR Operator
# --------------------------------------------------

is_weekend = False
is_holiday = True

if is_weekend or is_holiday:
    print("You can relax today...")
else:
    print("Go to work.")


# --------------------------------------------------
# Example 3: NOT Operator
# --------------------------------------------------

is_logged_in = False

if not is_logged_in:
    print("Please login first")
else:
    print("Welcome!")


# --------------------------------------------------
# Example 4: Login Access Check
# --------------------------------------------------

username_correct = True
password_correct = False

if username_correct and password_correct:
    print("Login successful!")
else:
    print("Invalid username or password....!")


# --------------------------------------------------
# Example 5: Temperature Check
# --------------------------------------------------

temperature = 35

if temperature > 30 and temperature < 40:
    print("Weather is hot but manageable")
else:
    print("Temperature is extreme")



# --------------------------------------------------
# Example 6: Complex Condition
# --------------------------------------------------


age = 16
has_permission = True
has_ticket = True

if (age >= 18 and has_ticket) or (has_permission and has_ticket):
    print("You can enter the event!")
else:
    print("Entry not allowed")
