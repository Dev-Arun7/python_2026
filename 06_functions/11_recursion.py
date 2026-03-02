"""
--------------------------------------------------
RECURSION IN PYTHON - SIMPLE EXAMPLE
--------------------------------------------------

Recursion = A function calling itself.

Important:
1. Must have a base case (stopping condition)
2. Must move toward the base case
"""

# --------------------------------------------------
# Example 1️⃣ - Factorial using Recursion
# --------------------------------------------------

def factorial(n: int) -> int:
    """
    Returns factorial of a number using recursion.

    Example:
    5! = 5 × 4 × 3 × 2 × 1
    """

    # Base case (stopping condition)
    if n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)


print("Factorial Example:")
print("5! =", factorial(5))


# --------------------------------------------------
# Example 2️⃣ - Simple Countdown
# --------------------------------------------------

def countdown(n: int) -> None:
    """
    Prints numbers from n to 1 using recursion.
    """

    # Base case
    if n == 0:
        print("Done!")
        return

    print(n)

    # Recursive call
    countdown(n - 1)


print("\nCountdown Example:")
countdown(5)