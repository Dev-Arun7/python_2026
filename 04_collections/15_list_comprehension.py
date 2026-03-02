"""
List comprehension = a concise way to create list in python
                    compact and easier to read than traditional loop method
                    [expression  for value in iterable if condition]
"""

# Traditiona method to find double
nums = [1, 5, 4,  7, 3, 9, 6, 4]
doubles = []
for n in nums:
    doubles.append(n * 2) # double each number and append to list

print(doubles)


# List comprehension
comp_doubles = [x * 2 for x in nums]
print(comp_doubles) 


# Another example
fruits = ["apple", "mango", "orange", "banana"]
starting_letter = [fruit[0] for fruit in fruits]
print(starting_letter)


# find positive
nums = [-1, 7, -6, 4, -5, 9]
positives = [x for x in nums if x >= 0]
print(positives)


# Doubles of evens
even_doubles = [x *2 for x in nums if x % 2 == 0]
print(even_doubles)
