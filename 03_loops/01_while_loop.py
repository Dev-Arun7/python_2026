# --------------------------------------------------
# WHILE LOOP PRACTICE
# while loop runs while condition is True
# --------------------------------------------------


# --------------------------------------------------
# Example 1: Password check
# Loop keeps asking until correct password is entered
# --------------------------------------------------

original_password = "123arun"

password = input("Enter the password: ")

while password != original_password:
    print("Enter correct password...!")
    password = input("Enter the password: ")

print("Password is correct, welcome user 🙂")


# --------------------------------------------------
# Example 2: Age validation
# Prevent negative age input
# --------------------------------------------------

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be a negative number...!")
    age = int(input("Enter your age: "))

print(f"Your age is {age}")


# --------------------------------------------------
# Example 3: Food list until user quits
# Loop stops when user enters 'q'
# --------------------------------------------------

food = input("Enter a food you like (q for quit): ")

while food != "q":
    print(f"You like {food}")
    food = input("Enter another food: ")

print("Bye 👋")


# --------------------------------------------------
# Example 4: Number range validation
# Ask until user enters number between 1 and 10
# --------------------------------------------------

num = int(input("Enter a number between 1 and 10: "))

while num < 1 or num > 10:
    print("Invalid number ❌")
    num = int(input("Enter a number between 1 and 10: "))

print(f"You entered {num} ✅")
