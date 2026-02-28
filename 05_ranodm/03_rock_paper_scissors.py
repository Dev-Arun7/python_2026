"""
Rock Paper Scissors Game
Simple version for beginners
"""

import random

# We use tuple because we don't need to change these values
options = ("rock", "paper", "scissors")

# This variable controls the game loop
running = True

while running:

    # Reset player value each round
    player = ""
    
    # Computer randomly selects one option
    computer = random.choice(options)

    # Keep asking until user gives correct input
    while player not in options:
        player = input("Enter a choice (rock, paper, scissors): ").lower()

        # If user enters wrong value
        if player not in options:
            print("Invalid choice! Please try again.\n")

    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}\n")

    # Check for tie
    if player == computer:
        print("It's a tie!")

    # Check winning conditions
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")
    elif player == "scissors" and computer == "paper":
        print("You win!")

    # If none of the above, player loses
    else:
        print("You lose!")

    # Ask if user wants to play again
    play_again = input("\nPlay again? (y/n): ").lower()

    # Stop the loop if user does not type 'y'
    if play_again != "y":
        running = False
        print("Bye... 👋")