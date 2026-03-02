"""
--------------------------------------------------
INNER FUNCTIONS, LOCAL & GLOBAL VARIABLES
--------------------------------------------------
"""

# --------------------------------------------------
# GLOBAL VARIABLE
# --------------------------------------------------

message = "I am Global"

print("Global variable outside function:", message)


# --------------------------------------------------
# FUNCTION WITH LOCAL VARIABLE
# --------------------------------------------------

def show_message():
    # This is a LOCAL variable
    message = "I am Local"
    print("Inside function (Local):", message)


show_message()

# Global variable remains unchanged
print("After function call:", message)


print("\n" + "-" * 60)


# --------------------------------------------------
# USING GLOBAL KEYWORD
# --------------------------------------------------

count = 0  # Global variable

def increase_count():
    global count   # Tell Python to use global variable
    count += 1
    print("Inside function, count =", count)


increase_count()
increase_count()

print("Outside function, count =", count)


print("\n" + "-" * 60)


# --------------------------------------------------
# INNER FUNCTION (Function inside function)
# --------------------------------------------------

def outer_function(name):

    print("Outer function started")

    # Inner function
    def inner_function():
        print("Hello", name)   # Accessing outer variable

    inner_function()  # Calling inner function

    print("Outer function finished")


outer_function("Arun")


print("\n" + "-" * 60)


# --------------------------------------------------
# Example Showing Local Scope
# --------------------------------------------------

def test_scope():
    local_var = 100
    print("Inside function:", local_var)

test_scope()

# This will give error if uncommented
# print(local_var)
# ❌ NameError: local_var is not defined