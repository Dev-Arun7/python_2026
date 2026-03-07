"""
--------------------------------------------------
SCRIPT 2
--------------------------------------------------

🧠 Important Concept:

__name__ is a special variable in Python.

If you RUN this file directly:
    python script_2.py
Then:
    __name__ = "__main__"

If this file is IMPORTED:
    import script_2
Then:
    __name__ = "script_2"
"""


def drink(drink):
    print(f"Your favorite drink is {drink}..!")


def main():
    print("Running from script_2")
    drink("cola")


# This runs ONLY when this file is executed directly
if __name__ == '__main__':
    main()


print("script_2 loaded..") # This will print when this module called somewhere, 
# but fuctions never never execute unless it called intentionally