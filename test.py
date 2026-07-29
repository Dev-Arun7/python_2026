
# Reading input values from user.

name = input("Enter your name:")
age = input("Enter your age:")
int_age = int(age)
weight = float(input("Weight ?"))  # Converting directly

#--------------------------------
# What is happening above
# age = "33"
# int_age = 33
#--------------------------------

# Result
print(f"Hi {name} how's it going...., you're {age} year old now")
print(type(int_age))

