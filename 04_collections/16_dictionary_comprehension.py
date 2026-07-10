"""
Dictionary comprehension = a concise way to create dictionaries in python
                           compact and easier to read than traditional loop method
                           {key: value for value in iterable if condition}
"""

# Traditional method
nums = [1, 5, 4, 7, 3, 9, 6, 4]

square_dict = {}

for n in nums:
    square_dict[n] = n * n

print(square_dict)


# Dictionary comprehension
comp_square_dict = {x: x * x for x in nums}
print(comp_square_dict)


# Another example
fruits = ["apple", "mango", "orange", "banana"]

fruit_length = {fruit: len(fruit) for fruit in fruits}

print(fruit_length)


# Uppercase values
fruits = ["apple", "mango", "orange", "banana"]

upper_fruits = {fruit: fruit.upper() for fruit in fruits}

print(upper_fruits)


# Find positive numbers only
nums = [-1, 7, -6, 4, -5, 9]

positive_square = {x: x * x for x in nums if x > 0}

print(positive_square)


# Double only even numbers
nums = [1, 5, 4, 7, 3, 9, 6, 4]

even_doubles = {x: x * 2 for x in nums if x % 2 == 0}

print(even_doubles)


# Create dictionary from two lists
names = ["Arun", "Akhil", "Rahul"]
ages = [33, 30, 28]

people = {name: age for name, age in zip(names, ages)}

print(people)


# Swap keys and values
capitals = {
    "India": "New Delhi",
    "Japan": "Tokyo",
    "France": "Paris"
}

reverse = {value: key for key, value in capitals.items()}

print(reverse)


# Use if...else
nums = [1, 2, 3, 4, 5, 6]

result = {x: "Even" if x % 2 == 0 else "Odd" for x in nums}

print(result)