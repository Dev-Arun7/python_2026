"""
map()

map() applies a given function to every item in a collection.

Syntax:

    map(function, collection)

map() returns a map object, so we can convert it into a list
using list().
"""


# Function to convert Celsius to Fahrenheit
def c_to_f(temp):
    return (temp * 9 / 5) + 32


celsius_temps = [0.0, 10.0, 20.0, 30.0, 40.0, 50.0]


# map() applies c_to_f() to every item in celsius_temps.
fahrenheit_temps = map(c_to_f, celsius_temps)

print(list(fahrenheit_temps))


# ------------ Another way (commonly used) -----------------

# Instead of creating a separate function, we can use lambda
# directly inside map().
fahrenheit_temps = map(lambda temp: (temp * 9 / 5) + 32, celsius_temps)

print(list(fahrenheit_temps))


"""
HOW IT WORKS
------------

This:

    map(c_to_f, celsius_temps)

means:

    Apply c_to_f() to every item in celsius_temps.


For example:

    0.0  → 32.0
    10.0 → 50.0
    20.0 → 68.0
    30.0 → 86.0
    40.0 → 104.0
    50.0 → 122.0


map() returns a map object:

    fahrenheit_temps = map(c_to_f, celsius_temps)

To see the results as a list:

    list(fahrenheit_temps)


Using lambda:

    map(lambda temp: (temp * 9 / 5) + 32, celsius_temps)

Here, the lambda function is applied to every item
in the collection.


Simple idea:

    Collection
        ↓
    map()
        ↓
    Function applied to each item
        ↓
    New results


Example:

    [1, 2, 3, 4]
         ↓
        map()
         ↓
    [2, 4, 6, 8]
"""