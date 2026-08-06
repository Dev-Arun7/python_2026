# indexing = accessing elements of a sequence using [] (indexing operator)
# syntax:   [start: end : step]

credit_number = "1234-5678-9087-3456"


# Accessing the first number
print(credit_number[0])

# Accessing the 3rd number
print(credit_number[2])

# Accessing the last number
print(credit_number[-1])

# Accessing the third one from last
print(credit_number[-3])

# ------------------------------------------

# Accessing 2nd to 6th
print(credit_number[1 : 6])

# Accessing from beginning to 4th
print(credit_number[:4])

# Accessing all letters after 5th one
print(credit_number[5:])

# Access last 4 digits of credit card
last_digit = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digit}")

# ------------------------------------------

# Accessing 2nd to 10th one after another
print(credit_number[2:10:2])

# Access all numbers but each second one
print(credit_number[::2])

# Print the numbers in reverse order
print(credit_number[::-1])

