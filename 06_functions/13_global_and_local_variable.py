"""
global and local variable
"""

a = 10

def example():
    print(f"Printing inside the funciton: {a}") # printing outside variable (global variable)


example()
print(f"Printing outside the function: {a}")


#-------------------------------------------------------------------

b = 7
def example_1():
    b = 15 # Local variable
    print(f"Printing inside the funciton: {b}") # printing local variable


example()
print(f"Printing outside the function: {b}") # print global variable
