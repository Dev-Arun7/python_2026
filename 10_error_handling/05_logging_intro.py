"""
------------------------------------------------------------------------
Note: This topic is important for real-world projects.
But for now, learn only the basics.
------------------------------------------------------------------------

What is Logging?

Normally we use print() to show messages.

But in real applications:
- We don’t use too many print statements
- We store messages in a file
- We track errors properly

This is called Logging.
"""

# ---------------------------------------------------
# Step 1: Import logging module

import logging


# ---------------------------------------------------
# Step 2: Basic logging configuration

"""
basicConfig() sets:
- File name
- Logging level
- Format of message
"""

logging.basicConfig(
    filename="app.log",        # Log file name
    level=logging.DEBUG,       # Minimum level to track
    format="%(levelname)s - %(message)s"
)

# Now logs will be saved inside app.log file


# ---------------------------------------------------
# Example 1: Different logging levels

print("Example 1: Logging messages")

logging.debug("This is a DEBUG message.")
logging.info("This is an INFO message.")
logging.warning("This is a WARNING message.")
logging.error("This is an ERROR message.")
logging.critical("This is a CRITICAL message.")

print("Check the file 'app.log' to see logged messages.\n")


# ---------------------------------------------------
# Example 2: Logging inside try-except

print("Example 2: Logging errors")

try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print("Result:", result)

except ValueError:
    logging.error("User entered invalid input (not a number).")
    print("Invalid input!")

except ZeroDivisionError:
    logging.error("User tried to divide by zero.")
    print("Cannot divide by zero!")

print("Program finished 😊")