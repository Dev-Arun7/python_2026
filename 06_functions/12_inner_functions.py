"""
--------------------------------------------------
INNER FUNCTIONS, LOCAL & GLOBAL VARIABLES
--------------------------------------------------

This script explains:

1. Inner function not called
2. Inner function called inside outer
3. Returning inner function
4. Returning inner function with parameter
"""

# --------------------------------------------------
# 1️⃣ Inner Function NOT Called
# --------------------------------------------------

def outer():
    print("Printing from outer function.")

    def inner():
        print("Printing from inner function")

    # inner() is NOT called here


print("Example 1:")
outer()   # Only outer runs


print("\n" + "-" * 60)


# --------------------------------------------------
# 2️⃣ Calling Inner Function Inside Outer
# --------------------------------------------------

def outer_1():
    print("Printing from outer_1.")

    def inner():
        print("Printing from inner function")

    inner()   # Inner function is called here


print("Example 2:")
outer_1()   # Both outer and inner run


print("\n" + "-" * 60)


# --------------------------------------------------
# 3️⃣ Returning Inner Function
# --------------------------------------------------

def outer_2():
    print("Printing from outer_2.")

    def inner():
        print("Printing from inner function_2")

    return inner   # Returning function (not calling it)


print("Example 3:")

inner_function = outer_2()   # outer_2() executes here
inner_function()             # Now inner runs


"""
Explanation:
✔ outer function executes
✔ inner function is created
✔ inner function is returned
✔ inner function runs only when you call it
"""


print("\n" + "-" * 60)


# --------------------------------------------------
# 4️⃣ Returning Inner Function With Parameter
# --------------------------------------------------

def outer_3():
    print("Printing from outer_3.")

    def inner(num):
        print(f"The value is {num}")

    return inner   # Returning function


print("Example 4:")

inner_function = outer_3()   # outer_3 executes
inner_function(5)            # Passing value to inner