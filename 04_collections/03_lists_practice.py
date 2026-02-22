"""
--------------------------------------------------
LIST PRACTICE (BEGINNER EXERCISES)
--------------------------------------------------

Try solving each task yourself first.
Then run to verify output.

Exercises included:
1) Add items
2) Remove items safely
3) Count & search
4) Replace values
5) Build a new list using a loop
"""

# Start list
fruits = ["apple", "mango", "orange", "grape", "banana"]
print("\nStarting list:", fruits)

# --------------------------------------------------
# Exercise 1: Add 2 fruits to the end
# --------------------------------------------------
fruits.append("kiwi")
fruits.append("papaya")
print("\nAfter adding 2 fruits:", fruits)

# --------------------------------------------------
# Exercise 2: Remove 'mango' safely (only if it exists)
# --------------------------------------------------
if "mango" in fruits:
    fruits.remove("mango")
print("\nAfter removing mango safely:", fruits)

# --------------------------------------------------
# Exercise 3: Check if 'banana' exists and print its index
# --------------------------------------------------
if "banana" in fruits:
    print("\nBanana index:", fruits.index("banana"))
else:
    print("\nBanana not found")

# --------------------------------------------------
# Exercise 4: Replace the first fruit with 'blueberry'
# --------------------------------------------------
fruits[0] = "blueberry"
print("\nAfter replacing first item:", fruits)

# --------------------------------------------------
# Exercise 5: Create a new list with only fruits that contain letter 'a'
# --------------------------------------------------
fruits_with_a = []
for fruit in fruits:
    if "a" in fruit:
        fruits_with_a.append(fruit)

print("\nFruits containing 'a':", fruits_with_a)

# --------------------------------------------------
# Bonus: Print fruits in reverse without modifying original
# --------------------------------------------------
print("\nReverse view (no change to original):", fruits[::-1])
print("Original still:", fruits)