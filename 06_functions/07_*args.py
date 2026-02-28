"""
--------------------------------------------------
*args IN PYTHON
--------------------------------------------------

Normally, a function has a fixed number of parameters.

But sometimes we don’t know how many arguments
the user will pass.

In that case, we use *args.

*args collects multiple arguments into a tuple.
"""
# --------------------------------------------------
# 1️⃣ Normal Function (Fixed number of arguments)
# --------------------------------------------------

def add_two_numbers(a, b):
    result = a + b
    return result

print("Add two numbers:")
print(add_two_numbers(5, 4))

# This will cause error:
# add_two_numbers(5, 4, 7)
# ❌ TypeError: takes 2 positional arguments but 3 were given


# --------------------------------------------------
# 2️⃣ Using *args (Unlimited arguments)
# --------------------------------------------------

def addition(*args):
    total = 0

    # args is a tuple
    for arg in args:
        total += arg

    return total


print("\nAddition with many numbers:")
print(addition(2, 4, 7, 1))
print(addition(10, 20))
print(addition(1, 2, 3, 4, 5, 6))


# --------------------------------------------------
# 3️⃣ Another Example – Full Name
# --------------------------------------------------

def full_name(*args):
    for arg in args:
        print(arg, end=" ")
    print()   # Added to move to next line after finish function


print("\nSingle name:")
full_name("Arun")

print("\nTwo names:")
full_name("Akhil", "Balakrishnan")

print("\nThree names:")
full_name("Dr", "Anila", "VR")