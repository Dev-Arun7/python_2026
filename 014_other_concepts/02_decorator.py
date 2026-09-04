"""
Using multiple decorators with arguments.
"""


# This is the first decorator.
def add_sprinkles(func):

    # *args and **kwargs allow the decorator to work
    # with functions that have arguments.
    def wrapper(*args, **kwargs):
        print("Sprinkles added")
        func(*args, **kwargs)

    return wrapper


# This is the second decorator.
def add_chocolate(func):

    def wrapper(*args, **kwargs):
        print("Chocolate added..")
        func(*args, **kwargs)

    return wrapper


# Multiple decorators can be applied to the same function.
@add_sprinkles
@add_chocolate
def get_icecream(flavor):
    print(f"Here's your {flavor} ice cream...")


get_icecream("vanilla")


"""
Output:

Sprinkles added
Chocolate added..
Here's your vanilla ice cream...


Important:

Decorators are applied from bottom to top.

    @add_sprinkles
    @add_chocolate
    def get_icecream():

is basically:

    get_icecream = add_sprinkles(add_chocolate(get_icecream))


So the order is:

    get_icecream()
          ↓
    add_sprinkles
          ↓
    add_chocolate
          ↓
    original get_icecream()


*args and **kwargs:

They allow the wrapper function to accept any arguments
and pass them to the original function.

Here:

    get_icecream("vanilla")

"vanilla" is passed through:

    wrapper(*args, **kwargs)
            ↓
    func(*args, **kwargs)
            ↓
    get_icecream(flavor)
"""