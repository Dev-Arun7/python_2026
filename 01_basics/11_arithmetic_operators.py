# Full Arithmetic Operators Example in Python
import math # Importing math module for additional functions



friends = 0
print("Initial number of friends:", friends)

# Addition
friends = friends + 1      # Normal addition
print("After friends = friends + 1:", friends)

friends += 2               # Shortcut addition
print("After friends += 2:", friends)

# Subtraction
friends = friends - 1      # Normal subtraction
print("After friends = friends - 1:", friends)

friends -= 1               # Shortcut subtraction
print("After friends -= 1:", friends)

# Multiplication
friends = friends * 3      # Multiply by 3
print("After friends = friends * 3:", friends)

friends *= 2               # Shortcut multiplication
print("After friends *= 2:", friends)

# Division
friends = friends / 2      # Normal division (always gives float)
print("After friends = friends / 2:", friends)

friends /= 2               # Shortcut division
print("After friends /= 2:", friends)

# Floor Division
friends = friends // 1     # Floor division (removes decimal)
print("After friends = friends // 1:", friends)

# Modulus (remainder)
friends = friends % 2
print("After friends = friends % 2 (remainder when divided by 2):", friends)

# Exponentiation (power)
friends = 2 ** 3           # 2 to the power 3
print("After friends = 2 ** 3:", friends)

friends **= 2               # Shortcut power (friends = friends ** 2)
print("After friends **= 2:", friends)



# Rounding example
number = 3.14159
result = round(number)
rounded_to_2_decimals = round(number, 2)
print("Rounded number:", result)
print("Rounded to 2 decimals:", rounded_to_2_decimals)

# Absolute value example
negative_number = -5
absolute_value = abs(negative_number)
print("Absolute value of -5:", absolute_value)

# Power example
base = 2
exponent = 4
power_result = pow(base, exponent)
print("2 to the power of 4:", power_result)

# Max and Min examples
a = 10
b = 20
c = 5
max_value = max(a, b, c)
min_value = min(a, b, c)
print("Maximum value :", max_value)
print("Minimum value :", min_value)

# Square root example
number = 16
sqrt_result = math.sqrt(number)
print("Square root of 16:", sqrt_result)

# Ceiling and Floor examples
decimal_number = 3.7
ceiling_value = math.ceil(decimal_number)
floor_value = math.floor(decimal_number)
print("Ceiling of 3.7:", ceiling_value)
print("Floor of 3.7:", floor_value)


