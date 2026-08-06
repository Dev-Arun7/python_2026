# Ternary Operator
# A ternary operator is a short way to write an if-else statement in one line.

# Syntax:
# value_if_true if condition else value_if_false


# --------------------------------------------------
# Example 1: Simple Age Check
# --------------------------------------------------

age = 20

result = "Adult" if age >= 18 else "Minor"
print("Age check result:", result)


# --------------------------------------------------
# Example 2: Even or Odd Number
# --------------------------------------------------

number = 7

result = "Even" if number % 2 == 0 else "Odd"
print("Number is:", result)


# --------------------------------------------------
# Example 3: Pass or Fail
# --------------------------------------------------

marks = 45

result = "Pass" if marks >= 40 else "Fail"
print("Exam result:", result)


# --------------------------------------------------
# Example 4: Maximum of Two Numbers
# --------------------------------------------------

a = 10
b = 25

maximum = a if a > b else b
print("Maximum number is:", maximum)

# --------------------------------------------------
# Example 5: Login Status
# --------------------------------------------------

is_logged_in = True

message = "Welcome back!" if is_logged_in else "Please log in"
print(message)


# --------------------------------------------------
# Example 6: Nested Ternary (use carefully)
# --------------------------------------------------

score = 85

grade = "A" if score >= 80 else "B" if score >= 60 else "C"
print("Grade is:", grade)
