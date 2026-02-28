"""
====================================================
DEFAULT ARGUMENTS + POSITIONAL ARGUMENTS
====================================================

If a function has:

1. Normal (positional) arguments
2. Default arguments

Then the rule is:

👉 Default arguments must come AFTER normal arguments.

Correct:
    def test(a, b=10):

Wrong:
    def test(a=10, b):
"""

import time


# ====================================================
# Example: Simple Countdown with Delay
# ====================================================

def time_delay(end, start=0):
    """
    end   → required (positional argument)
    start → optional (default value = 0)
    """

    for x in range(start, end + 1):
        print(x)
        time.sleep(1) 

    print("Done")


# ====================================================
# 1️⃣ Calling with only required argument
# ====================================================

# Here:
# end = 5
# start = 0 (default value used)

print("Example 1:")
time_delay(5)


# ====================================================
# 2️⃣ Overriding default value
# ====================================================

# Here:
# end = 10
# start = 5 (we changed default)

print("\nExample 2:")
time_delay(10, 5)


# ====================================================
# IMPORTANT RULE EXPLANATION
# ====================================================

# Correct function definition
def example(a, b=100):
    return a + b


# ❌ This would cause error:
# def example(a=100, b):
#     return a + b


# ====================================================
# SUMMARY
# ====================================================

# 1. Required (positional) arguments must come first.
# 2. Default arguments must come after them.
# 3. If we don't pass a value, default is used.
# 4. If we pass a value, default is replaced.
#
# Think like:
# Default argument = Pre-set setting
# If you don't change it, default runs.
# If you change it, your value runs.
# ====================================================