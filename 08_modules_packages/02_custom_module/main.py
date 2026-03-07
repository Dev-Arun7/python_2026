"""
--------------------------------------------------
MAIN FILE
File Name: main.py
--------------------------------------------------

We are using functions from my_module.py

🧠 What is happening here?

Step 1:
When we write → import my_module
Python looks for a file named my_module.py

Step 2:
Python runs my_module.py once.

Step 3:
All variables and functions inside that file
become available through:

my_module.variable_name
my_module.function_name
"""

import my_module


print("-" * 50)

# Accessing variable from module
print("Value of PI:", my_module.pi)

print("-" * 50)

num = 2
radius = 5


# Calling square function
result_1 = my_module.squar(num)
print("Square:", result_1)


# Calling cube function
result_2 = my_module.cube(num)
print("Cube:", result_2)


# Calling circumference function
result_3 = my_module.circumferance(radius)
print("Circumference:", result_3)


# Calling area function
result_4 = my_module.area(radius)
print("Area:", result_4)


print("-" * 50)

"""
🧠 Important Understanding:

my_module.squar(2)

Breakdown:
- my_module → the imported file
- squar → function inside that file
- (2) → value passed to that function

Python connects main.py and my_module.py
using the import system.


Note: folder stucture should be:
📁 Folder
    ├── my_module.py
    └── main.py
"""


