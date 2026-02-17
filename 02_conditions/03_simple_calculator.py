# A simple calculator that performs basic arithmetic operations based on user input.


operator = input("Enter an operator (+, -, *, /):  ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation based on the operator
if operator == '+':
    result = round(num1 + num2, 2)
    print(f"The result of {num1} + {num2} is: {result}")
elif operator == '-':
    result = round(num1 - num2, 2)
    print(f"The result of {num1} - {num2} is: {result}")
elif operator == '*':
    result = round(num1 * num2, 2)
    print(f"The result of {num1} * {num2} is: {result}")
elif operator == '/':
    if num2 != 0:
        result = round(num1 / num2, 2)
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use one of +, -, *, or /.")