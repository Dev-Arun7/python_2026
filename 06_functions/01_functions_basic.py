"""
-----------------------------------------
WHAT IS A FUNCTION IN PYTHON?
-----------------------------------------

A function is a block of code that we can reuse.

Think like this:

Instead of writing the same code again and again,
we put it inside a function.

Then we can "call" (run) that function anytime we want.

Why use functions?

1. Avoid repeating code
2. Make code clean and readable
3. Easy to change later
-----------------------------------------
"""


# -----------------------------------------
# STEP 1: Define (Create) a Function
# -----------------------------------------

def happy_birthday():
    # The code inside this function will run
    # only when we call the function

    print("Happy birthday to you...")
    print("You are older now.")
    print("Happy happy birthday to you...")


# IMPORTANT:
# Just defining the function will NOT run it.
# We must CALL the function to execute it.


# -----------------------------------------
# STEP 2: Call (Run) the Function
# -----------------------------------------

print("Calling function one time:\n")
happy_birthday()   # This runs the function one time


# -----------------------------------------
# STEP 3: Calling Multiple Times
# -----------------------------------------

print("\nCalling function three times manually:\n")

happy_birthday()
happy_birthday()
happy_birthday()


# -----------------------------------------
# STEP 4: Calling Using a Loop
# -----------------------------------------

print("\nCalling function three times using a loop:\n")

for i in range(3):
    happy_birthday()



# ------------------------------------------------
# IMPORTANT NOTE
# ------------------------------------------------
# If we change the function once,
# the result changes everywhere.
#
# In this program, we called the function
# many times (manually and using a loop).
#
# But the actual code exists only ONE time
# inside the function.
#
# So if we change something inside the function,
# all calls will automatically use the new version.
#
# This is the real power of functions.
# Write once → Use many times.
# Change once → Update everywhere.
# ------------------------------------------------