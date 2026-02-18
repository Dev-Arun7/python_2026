# --------------------------------------------------
# FOR LOOP LEARNING SCRIPT
# A for loop runs a block of code a fixed number of times
# You can iterate over range, string, list, etc.
# --------------------------------------------------


# --------------------------------------------------
# Example 1: Print numbers from 1 to 10
# range(start, stop) → stop is NOT included
# --------------------------------------------------

print("Numbers from 1 to 10:\n")

for x in range(1, 11):
    print(x)

# Runs after loop finishes
print("HAPPY NEW YEAR 🎉")


# --------------------------------------------------
# Example 2: Step value
# range(start, stop, step)
# Here it increases by 5 each time
# --------------------------------------------------

print("\nNumbers from 0 to 95 with step 5:\n")

for x in range(0, 100, 5):
    print(x)


# --------------------------------------------------
# Example 3: Loop through a string
# Each character is printed one by one
# --------------------------------------------------

print("\nLoop through credit card string:\n")

credit_card = "1234-5678-9098-5432"

for num in credit_card:
    print(num)


# --------------------------------------------------
# continue vs break
# continue → skip current iteration and go to next
# break → stop loop completely
# --------------------------------------------------


# --------------------------------------------------
# Example 4: Skip number 7 using continue
# --------------------------------------------------

print("\nSkip number 7:\n")

for x in range(1, 10):
    if x == 7:
        continue
    print(x)


# --------------------------------------------------
# Example 5: Stop loop when number is 7
# --------------------------------------------------

print("\nStop when number is 7:\n")

for x in range(1, 10):
    if x == 7:
        break
    print(x)


# --------------------------------------------------
# Exercise: Check if phone number contains invalid characters
# If any character is not a digit → show warning
# --------------------------------------------------

print("\nPhone number validation:\n")

phone_number = "123245%6789"

for x in phone_number:
    if not x.isdigit():
        print("Invalid number ❌ — non digit character found")
        break   # stop after first invalid character
