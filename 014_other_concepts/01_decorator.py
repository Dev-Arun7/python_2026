"""
Decorator

A decorator is a function that extends the behavior of another
function without modifying the original function.

The original function is passed to the decorator as an argument.
"""


# This is the decorator function.
# It receives another function as an argument.
def add_sprinkles(func):

    # This wrapper function adds extra behavior
    # before calling the original function.
    def wrapper():
        print("Sprinkles added")

        # Call the original function
        func()

    # Return the wrapper function
    return wrapper


# @add_sprinkles applies the decorator to get_icecream().
# It is basically the same as:
# get_icecream = add_sprinkles(get_icecream)
@add_sprinkles
def get_icecream():
    print("Here's your ice cream...")


# Calling get_icecream() actually calls the wrapper function.
get_icecream()


"""
How it works:

1. Python sees:

       @add_sprinkles
       def get_icecream():

2. Python passes get_icecream to add_sprinkles():

       add_sprinkles(get_icecream)

3. Inside add_sprinkles(), the original function is stored
   in the variable 'func'.

4. The decorator creates the wrapper() function.

5. wrapper() adds extra behavior:

       print("Sprinkles added")

6. Then wrapper() calls the original function:

       func()

7. Finally, the wrapper function is returned.

So when we call:

       get_icecream()

the flow is:

       get_icecream()
             ↓
          wrapper()
             ↓
       Sprinkles added
             ↓
          func()
             ↓
       Here's your ice cream...


Output:

Sprinkles added
Here's your ice cream...


Simple definition:

Decorator = A function that adds extra behavior to another
function without changing the original function's code.
"""