"""
Creating a Python Number Guessing Game 🎯
"""

import random  # Import random module to generate random number

low = 1
high = 100

guesses = 0          # Counter to track number of attempts (valid + invalid)
is_running = True    # Control variable for while loop

# Generate random number between low and high
answer = random.randint(low, high)

print("Welcome to the number guessing game...")

# Take first input before loop starts
value = input(f"Enter your guess between {low} and {high}: ")

# Game loop
while is_running:

    # Check if input is a number
    if value.isdigit():

        guess = int(value)  # Convert string input to integer

        # Check if number is outside allowed range
        if guess < low or guess > high:
            print("Entered value is out of range...!")
            value = input(f"Please enter a value between {low} and {high}: ")

        # Guess is smaller than answer
        elif guess < answer:
            print("The value is too low.")
            value = input(f"Please enter a value between {low} and {high}: ")

        # Guess is greater than answer
        elif guess > answer:
            print("The value is too high.")
            value = input(f"Please enter a value between {low} and {high}: ")

        # Correct guess 🎉
        else:
            print(f"Winner 🎉, you took {guesses} guesses")
            break

    else:
        # Input is not a number
        print("Entered value is not valid...!")
        value = input(f"Please enter a value between {low} and {high}: ")

    # Increase guess counter every loop iteration
    guesses += 1