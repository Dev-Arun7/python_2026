"""
--------------------------------------------------
MEMBERSHIP OPERATORS IN PYTHON
--------------------------------------------------

Membership operators are used to check
whether a value exists in a sequence.

Operators:
1. in
2. not in
"""

# --------------------------------------------------
# 1️⃣ Using "in" with String
# --------------------------------------------------

name = "ARUN BALAKRISHNAN"

letter = input("Enter a letter to check in name: ")

if letter in name:
    print(f"The letter '{letter}' is found in the name.")
else:
    print(f"The letter '{letter}' is NOT found in the name.")


print("\n" + "-" * 50)


# --------------------------------------------------
# 2️⃣ Using "in" with List
# --------------------------------------------------

fruits = ["apple", "mango", "banana", "orange"]

fruit = input("Enter a fruit name: ")

if fruit in fruits:
    print(f"{fruit} is in the list.")
else:
    print(f"{fruit} is NOT found in the list.")


print("\n" + "-" * 50)


# --------------------------------------------------
# 3️⃣ Using "not in" with String
# --------------------------------------------------

sentence = "YOU ARE AWESOME"

letter = input("Enter a letter to check in sentence: ")

if letter not in sentence:
    print(f"The letter '{letter}' is NOT found in the sentence.")
else:
    print(f"The letter '{letter}' is found in the sentence.")


print("\n" + "-" * 50)


# --------------------------------------------------
# 4️⃣ Using with Dictionary
# --------------------------------------------------

person = {
    "name": "Arun",
    "age": 25,
    "city": "Kannur"
}

key = input("Enter a key to check in dictionary: ")

if key in person:
    print(f"'{key}' key exists in dictionary.")
else:
    print(f"'{key}' key does NOT exist.")


print("\n" + "-" * 50)


# --------------------------------------------------
# 5️⃣ Using with Set
# --------------------------------------------------

numbers = {10, 20, 30, 40}

num = int(input("Enter a number to check in set: "))

if num in numbers:
    print(f"{num} is present in the set.")
else:
    print(f"{num} is NOT present in the set.")


print("\nProgram Finished ✅")




"""
--------------------------------------------------
NOTES ABOUT 'in' AND 'not in'
--------------------------------------------------

1. 'in'
   - Returns True if value exists.
   - Returns False if value does not exist.

2. 'not in'
   - Returns True if value does NOT exist.
   - Returns False if value exists.

3. Works with:
   - String
   - List
   - Tuple
   - Set
   - Dictionary (checks only KEYS)

4. Important:
   In dictionary:
       if key in dictionary:
   checks keys only.

   To check values:
       if value in dictionary.values():

5. Membership operators return Boolean values:
   True or False
"""