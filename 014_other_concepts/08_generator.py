"""
Generator

A generator is a special type of iterator that produces values
one at a time using the yield keyword.

Generators are useful when working with large amounts of data
because they do not store all values in memory at once.
"""


# ===========================================================
# Normal function
# ===========================================================

def count_to(n):
    numbers = []
    count = 1

    while count <= n:
        numbers.append(count)
        count += 1

    return numbers


n = 10

for i in count_to(n):
    print(i)


# ===========================================================
# Same example using a generator
# ===========================================================

def count_to_new(n):
    count = 1

    while count <= n:
        yield count  # Produce one value and pause here
        count += 1


n = 10

for i in count_to_new(n):
    print(i)


"""
HOW IT WORKS
------------
Normal function:

    count_to()

creates a list containing all the numbers:

    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Then return sends the complete list back.


Generator:

    count_to_new()

uses yield instead of return.

    yield count

produces one value at a time.

After yielding a value, the function pauses.

When the next value is requested, it continues from
where it stopped.


RETURN vs YIELD
---------------
return:
    Sends back the result and finishes the function.

yield:
    Sends back one value and pauses the function.


MEMORY
------
Normal function:

    Creates all values
        ↓
    Stores them in a list
        ↓
    Returns the list


Generator:

    Create one value
        ↓
      yield
        ↓
    Pause
        ↓
    Create next value
        ↓
      yield
        ↓
    Pause
        ↓
       ...


IMPORTANT
---------
A function containing yield becomes a generator function.

Calling:

    count_to_new(10)

does not immediately create all 10 numbers.

The values are generated when we iterate over the generator.


Simple idea:

    Normal function → creates everything → return

    Generator      → creates one at a time → yield
"""