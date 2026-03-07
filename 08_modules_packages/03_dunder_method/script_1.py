"""
--------------------------------------------------
SCRIPT 1
--------------------------------------------------

🧠 What is happening here?

1) We import script_2
2) When importing, Python runs script_2 from top to bottom.
3) But script_2's main() will NOT run (because of __name__ check).
4) Then this file continues execution.
"""

import script_2   # Python loads script_2 here

print("module imported")  # This runs after script_2 is loaded


def food(food):
    print(f"Your favorite food is {food}..!")


def main():
    print("Running from script_1")

    food("pizza")

    # Calling function from script_2
    script_2.drink("sprite")

    print("completed")


# This runs ONLY if we execute script_1 directly
if __name__ == '__main__':
    main()