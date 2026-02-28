"""
====================================================
RETURN STATEMENT (COMPLETE BEGINNER SCRIPT)
====================================================

Return = A function sends a value back after finishing its work.

Think like a machine:

Input  →  Machine works  →  Output comes out

That output is what we RETURN.

Important Difference:
print() → Only shows the value on screen
return  → Sends value back so we can store and use it
"""
# ====================================================
# 1️⃣ BASIC MATH FUNCTIONS
# ====================================================

def add(x, y):
    z = x + y
    return z


def subtract(x, y):
    z = x - y
    return z


def mul(x, y):
    z = x * y
    return z


def divide(x, y):

    # Prevent division by zero
    if y == 0:
        return "Cannot divide by zero"

    z = x / y
    return z


# ====================================================
# 2️⃣ USING RETURNED VALUES
# ====================================================

num_1 = 8
num_2 = 2

result = add(num_1, num_2)
print("Addition result:", result)

print("Subtraction result:", subtract(10, 3))
print("Multiplication result:", mul(2, 4))
print("Division result:", divide(10, 2))
print("Division result:", divide(10, 0))

# ====================================================
# 3️⃣ RETURN VS PRINT DIFFERENCE
# ====================================================

def add_with_print(x, y):
    print(x + y)   # Only prints, does not return


def add_with_return(x, y):
    return x + y   # Returns value


print("\nUsing print inside function:")
add_with_print(5, 5)

print("\nUsing return inside function:")
value = add_with_return(5, 5)
print("Stored value:", value)

# We can even use returned value in calculation
total = add_with_return(5, 5) + 10
print("Total after adding 10:", total)

# ====================================================
# 4️⃣ REAL EXAMPLE – FORMATTING A NAME
# ====================================================

def create_name(first, last):

    first = first.capitalize()
    last = last.capitalize()

    return f"{first} {last}"


first_name = "arun"
last_name = "balakrishnan"

full_name = create_name(first=first_name, last=last_name)

print("\nFormatted full name:", full_name)


# ====================================================
# 5️⃣ HOW ARGUMENTS ARE PASSED
# ====================================================

# Method 1: By Position (Order matters)

print("\nBy Position:")
print(create_name("arun", "balakrishnan"))

# Here:
# First value goes to 'first'
# Second value goes to 'last'
# Order is important!


# Method 2: By Name (Order does NOT matter)

print("\nBy Name:")
print(create_name(last="balakrishnan", first="arun"))

# Here:
# We clearly mention which value goes where
# So order does not matter


# ====================================================
# IMPORTANT NOTES
# ====================================================
# 1. return sends value back to where function was called.
# 2. After return runs, function stops immediately.
# 3. You can store returned value in a variable.
# 4. You can use returned value in another calculation.
# 5. return makes functions powerful and reusable.
#
# Think like:
# Function = Machine
# return = Output from the machine
# ====================================================