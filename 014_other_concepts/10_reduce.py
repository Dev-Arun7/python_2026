"""
reduce()

reduce() repeatedly applies a function to the items in a collection
and reduces the collection to a single value.

reduce() is available from the functools module.

Syntax:
    reduce(function, collection)
"""

from functools import reduce


# ===========================================================
# Example: Find the sum of all numbers
# ===========================================================

numbers = [1, 2, 3, 4, 5]


def add(x, y):
    return x + y


result = reduce(add, numbers)

print(result)


# ===========================================================
# Using lambda
# ===========================================================

result = reduce(lambda x, y: x + y, numbers)

print(result)


"""
HOW IT WORKS
------------
Given:

    numbers = [1, 2, 3, 4, 5]

reduce() works like this:

    1 + 2 = 3
    3 + 3 = 6
    6 + 4 = 10
    10 + 5 = 15

Final result:

    15


NORMAL FUNCTION
---------------
This:

    reduce(add, numbers)

means:

    Take the first two values
        ↓
    Apply add()
        ↓
    Take the result and the next value
        ↓
    Apply add() again
        ↓
    Continue until all values are used


LAMBDA
------
We can also write:

    reduce(lambda x, y: x + y, numbers)

This does the same thing without creating a separate function.


IMPORTANT
---------
map():
    Changes every item.

filter():
    Selects items based on a condition.

reduce():
    Combines items into one final value.


Simple idea:

    [1, 2, 3, 4, 5]
            ↓
         reduce()
            ↓
            15
"""