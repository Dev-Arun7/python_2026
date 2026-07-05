# Type casting (type conversion) allows us to convert one data type to another. 
# This is useful when we want to perform operations that require specific types.
# Example: Converting a string to an integer ("5" to 5) so we can perform arithmetic operations.

name = "Anila"
age = 25
gpa = 3.2
is_student = True

# Checking types
print(type(name))  # <class 'str'>
print(type(age))   # <class 'int'>
print(type(gpa))   # <class 'float'>
print(type(is_student))  # <class 'bool'>


# print age with and without type casting
print(age)
print(float(age)) # Convert int to float
print(str(age))
print(int(gpa))


bool_value = bool(name)  # Non-empty string is always True
print(bool_value) 