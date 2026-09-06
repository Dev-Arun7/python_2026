"""
Iterator

An iterator is an object that allows us to go through a collection
one item at a time.

Important functions:
    iter()  → creates an iterator
    next()  → gets the next item
"""


# ===========================================================
# Creating an iterator from a list
# ===========================================================

nums = [7, 2, 3, 9, 1, 6, 5, 4]

it = iter(nums)

print(next(it))
print(next(it))
print(next(it))


# ===========================================================
# Creating our own iterator
# ===========================================================

class Top_ten:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration


values = Top_ten()

for i in values:
    print(i)


"""
HOW IT WORKS
------------
A list is an iterable:

    nums = [7, 2, 3, 9, 1, 6, 5, 4]

We can create an iterator from it:

    it = iter(nums)

Then use next() to get one item at a time:

    next(it)
    next(it)
    next(it)


ITERATOR METHODS
----------------
An iterator normally has two methods:

    __iter__()
        Returns the iterator itself.

    __next__()
        Returns the next item.

When there are no more items, __next__() raises:

    StopIteration


CUSTOM ITERATOR
---------------
Our Top_ten class creates numbers from 1 to 10.

    __iter__()
        Returns self.

    __next__()
        Returns the next number.

    self.num += 1
        Moves to the next number.


FOR LOOP
--------
A for loop automatically calls next() repeatedly.

So:

    for i in values:
        print(i)

roughly works like:

    1
    2
    3
    ...
    10

When __next__() raises StopIteration,
the for loop automatically stops.


IMPORTANT
---------
Iterable:
    An object that can be iterated over.

Examples:
    list
    tuple
    string
    dictionary

Iterator:
    An object that gives us items one at a time
    using next().


Simple idea:

    Iterable
       ↓
     iter()
       ↓
    Iterator
       ↓
     next()
       ↓
   One item at a time
"""