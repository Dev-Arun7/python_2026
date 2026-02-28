"""
Dice Game with Box Style Unicode 🎲
"""

import random

# Dictionary to store dice drawings
dice_art = {
    1: (
        "┌───────┐\n"
        "│       │\n"
        "│   ●   │\n"
        "│       │\n"
        "└───────┘"
    ),
    2: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│       │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    3: (
        "┌───────┐\n"
        "│ ●     │\n"
        "│   ●   │\n"
        "│     ● │\n"
        "└───────┘"
    ),
    4: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│       │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    5: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│   ●   │\n"
        "│ ●   ● │\n"
        "└───────┘"
    ),
    6: (
        "┌───────┐\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "│ ●   ● │\n"
        "└───────┘"
    )
}

running = True

while running:

    input("Press Enter to roll the dice 🎲 ")

    number = random.randint(1, 6)

    print("\nYou rolled:", number)
    print(dice_art[number])   # Print the box dice

    play_again = input("\nRoll again? (y/n): ").lower()

    if play_again != "y":
        running = False
        print("Game Over 👋")