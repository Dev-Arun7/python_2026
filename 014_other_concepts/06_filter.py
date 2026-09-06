"""
filter()

filter() is used to filter items from a collection based on a condition.

Syntax:
    filter(function, collection)

It keeps only the items for which the function returns True.
"""


# Function used by filter()
def is_passing(grade):
    return grade >= 60  # Return True if grade is 60 or higher


grades = [32, 98, 75, 41, 53, 86, 44, 91]


# Using a normal function
passing_grades = filter(is_passing, grades)

print(list(passing_grades))


# ------------ Another way using lambda -----------------

passing_grades = filter(lambda grade: grade >= 60, grades)

print(list(passing_grades))


"""
HOW IT WORKS
------------
filter() checks every item in the collection.

For example:

    filter(is_passing, grades)

means:

    Check each grade using is_passing()
    Keep the grade if it returns True.


Given:

    grades = [32, 98, 75, 41, 53, 86, 44, 91]

The result is:

    [98, 75, 86, 91]


Using lambda:

    filter(lambda grade: grade >= 60, grades)

This does the same thing without creating a separate function.


IMPORTANT
---------
filter() returns a filter object.

So we use:

    list(passing_grades)

to convert the result into a list.


Simple idea:

    Collection
        ↓
      filter()
        ↓
    Check condition
        ↓
    Keep items that return True
"""