# --------------------------------------------------
# FOR LOOP PRACTICE (BEGINNER LEVEL)
# No lists or collections used
# --------------------------------------------------


# --------------------------------------------------
# Example 1: Print numbers from 1 to 5
# --------------------------------------------------

print("Example 1: Numbers 1 to 5\n")

for i in range(1, 6):
    print(i)


# --------------------------------------------------
# Example 2: Print even numbers from 2 to 10
# --------------------------------------------------

print("\nExample 2: Even numbers\n")

for i in range(2, 11, 2):
    print(i)


# --------------------------------------------------
# Example 3: Countdown timer
# --------------------------------------------------

print("\nExample 3: Countdown\n")

for i in range(5, 0, -1):
    print(i)

print("Go 🚀")


# --------------------------------------------------
# Example 4: Print each letter in a word
# --------------------------------------------------

print("\nExample 4: Loop through string\n")

word = "python"

for letter in word:
    print(letter)


# --------------------------------------------------
# Example 5: Count total characters in a word
# --------------------------------------------------

print("\nExample 5: Count characters\n")

word = "developer"
count = 0

for letter in word:
    count += 1

print("Total characters:", count)


# --------------------------------------------------
# Example 6: Sum numbers from 1 to 5
# --------------------------------------------------

print("\nExample 6: Sum of numbers\n")

total = 0

for i in range(1, 6):
    total += i

print("Sum =", total)


# --------------------------------------------------
# Example 7: Find a letter in a word
# --------------------------------------------------

print("\nExample 7: Find letter 'a'\n")

text = "banana"

for letter in text:
    if letter == "a":
        print("Found 'a'")


# --------------------------------------------------
# Example 8: Simple multiplication table of 3
# --------------------------------------------------

print("\nExample 8: Table of 3\n")

for i in range(1, 11):
    print("3 x", i, "=", 3 * i)


# --------------------------------------------------
# END OF SCRIPT
# --------------------------------------------------
