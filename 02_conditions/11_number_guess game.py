# ---------------------------------------------------------
# MINI PROJECT: NUMBER GUESSING GAME
# User enter a number which compare with pre defined number
# Win the user if user guess the correct one
# ---------------------------------------------------------

# Secret number (Change it if you want)
secret_number = 7

print("🎮 Welcome to Number Guessing Game")
print("Guess a number between 1 and 10")
print("Type 'q' to quit\n")

# Start the loop
while True:
    user_input = input("Enter the number: ")

    # Allow user to quit
    if user_input == "q":
        print("Game ended. Bye 👋")
        break  # loop stops here

    # convert the number to int
    user_input = int(user_input)

    # Check the number
    if user_input == secret_number:
        print("🎉 Correct! You guessed the number!")
        break   # ✅ FIX: stop game when correct

    elif user_input < secret_number:   # Comparing wit variable
        print("Too low, try again...")

    elif user_input > secret_number:  
        print("Too high, try again....")





# ---------------------------------------------------------
# ABOUT "break"
# ---------------------------------------------------------
# break is used to immediately stop a loop.
#
# When Python sees "break", it exits the loop right away
# and continues running the code after the loop.
#
# We usually use break when:
# ✅ We found what we were looking for
# ✅ The user wants to quit
# ✅ A condition is satisfied
#
# In this program:
# break is used when the user guesses the correct number
# or when the user types "q" to quit the game.
#
# Without break, the loop would continue forever.
# ---------------------------------------------------------

