"""
Beginner-Friendly Python Lambda Examples
(Only basic usage – no map, no filter)

A lambda function is a small anonymous function.
It can take arguments but has only one expression.
The result is automatically returned.
"""

# ---------------------------------------------------
# Example 1: Double a number

# Normal function
def double(x):
    return x * 2

# Same using lambda
double_lambda = lambda x: x * 2

print("Double of 5:", double_lambda(5))


# ---------------------------------------------------
# Example 2: Add two numbers

addition = lambda x, y: x + y
print("4 + 6 =", addition(4, 6))


# ---------------------------------------------------
# Example 3: Find maximum of two numbers

max_value = lambda x, y: x if x > y else y
print("Max of 10 and 20:", max_value(10, 20))


# ---------------------------------------------------
# Example 4: Join two strings

full_name = lambda first, last: first + " " + last
print("Full Name:", full_name("Arun", "Balakrishnan"))


# ---------------------------------------------------
# Example 5: Check if number is even

is_even = lambda x: x % 2 == 0
print("Is 8 even?", is_even(8))
print("Is 7 even?", is_even(7))


# ---------------------------------------------------
# Example 6: Age category

age_check = lambda age: "Adult" if age >= 18 else "Minor"
print("Age 21:", age_check(21))
print("Age 15:", age_check(15))


# ---------------------------------------------------
# Slightly More Complex Example

# Calculate total price after discount
# If price > 1000, give 10% discount
# Otherwise, no discount

discount_price = lambda price: price * 0.9 if price > 1000 else price

print("Price 1500 after discount:", discount_price(1500))
print("Price 500 after discount:", discount_price(500))


# ---------------------------------------------------
# Lambda returning another lambda (little advanced but important)

def multiplier(n):
    return lambda x: x * n

double_func = multiplier(2)
triple_func = multiplier(3)

print("Double of 4:", double_func(4))
print("Triple of 4:", triple_func(4))