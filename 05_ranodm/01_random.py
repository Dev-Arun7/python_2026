"""
Learn basic random functions in Python 🎲
"""

import random  # Import random module


# ----------------------------------------
# Random integer between 1 and 6
# ----------------------------------------

number = random.randint(1, 6)
print("Random dice number:", number)


# ----------------------------------------
# Random integer between low and high
# ----------------------------------------

low = 1
high = 100

random_number = random.randint(low, high)
print("Random number between 1 and 100:", random_number)


# ----------------------------------------
# Random float between 0 and 1
# ----------------------------------------

random_float = random.random()
print("Random float:", random_float)


# ----------------------------------------
# Random choice from options
# ----------------------------------------

options = ("rock", "paper", "scissors") 

random_option = random.choice(options)
print("Random choice:", random_option)


# ----------------------------------------
# Shuffle a list
# ----------------------------------------

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

random.shuffle(cards)  # Shuffle happens in-place
print("Shuffled cards:", cards)