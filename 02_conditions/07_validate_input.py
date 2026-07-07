# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter username: ")

# Check length of the username
if len(username) > 12:
    print("Your username can't be more than 12 characters")

# Check for spaces
elif not username.find(" ") == -1: # Not equal to -1 means not white space
    print("Your username can't contain spaces")

# Check if only letters
elif not username.isalpha():
    print("Your username must contain letters only (no numbers or symbols)")
else:
    print(f"Welcome {username}")



