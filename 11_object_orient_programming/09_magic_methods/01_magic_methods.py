"""
Magic Methods in Python

Magic methods are special methods in Python that start and end
with double underscores.

Example:

    __init__
    __str__
    __eq__
    __lt__

They allow us to define how our objects behave when we use
Python's built-in operations such as:

    print()
    ==
    <
    >
    +
    in
    []

Magic methods are also called "dunder methods".

"Dunder" means:
    Double UNDERscore
"""


class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    # __str__
    # Controls what happens when we use print() with an object
    def __str__(self):
        return f"{self.title} by {self.author}"

    # __eq__
    # Controls how == works between two Book objects
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # __lt__
    # Controls how < works between two Book objects
    # Here, we compare the number of pages
    def __lt__(self, other):
        return self.num_pages < other.num_pages

    # __gt__
    # Controls how > works between two Book objects
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    # __add__
    # Controls how + works between two Book objects
    def __add__(self, other):
        return f"Total pages: {self.num_pages + other.num_pages}"

    # __contains__
    # Controls how the "in" operator works
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    # __getitem__
    # Controls how [] works with our object
    def __getitem__(self, key):
        if key == "title":
            return self.title

        if key == "author":
            return self.author

        if key == "pages":
            return self.num_pages

        # Raise an error if the key does not exist
        raise KeyError(f"Key '{key}' was not found!")


# Creating Book objects
book1 = Book("Atomic Habits", "James Clear", 232)
book2 = Book("The Psychology of Money", "Morgan Housel", 412)
book3 = Book("Python Crash Course", "Eric Matthes", 149)
book4 = Book("Deep Work", "Cal Newport", 756)


# --------------------------------------------------
# __str__
# --------------------------------------------------
# Normally Python doesn't know how we want our
# Book object to look when we print it.

print(book1)

# Python automatically calls:
# book1.__str__()


# --------------------------------------------------
# __eq__
# --------------------------------------------------
# Controls the == operator

print(book1 == book2)

# Python automatically calls:
# book1.__eq__(book2)


# --------------------------------------------------
# __lt__
# --------------------------------------------------
# Controls the < operator

print(book1 < book2)

# Python automatically calls:
# book1.__lt__(book2)


# --------------------------------------------------
# __gt__
# --------------------------------------------------
# Controls the > operator

print(book4 > book3)

# Python automatically calls:
# book4.__gt__(book3)


# --------------------------------------------------
# __add__
# --------------------------------------------------
# Controls the + operator

print(book1 + book2)

# Python automatically calls:
# book1.__add__(book2)


# --------------------------------------------------
# __contains__
# --------------------------------------------------
# Controls the "in" operator

print("James" in book1)
print("Python" in book3)

# Python automatically calls:
# book1.__contains__("James")


# --------------------------------------------------
# __getitem__
# --------------------------------------------------
# Controls the [] operator

print(book1["title"])
print(book1["author"])
print(book1["pages"])

# Python automatically calls:
# book1.__getitem__("title")
# book1.__getitem__("author")
# book1.__getitem__("pages")








"""
==========================================================
                    MAGIC METHODS
==========================================================

Magic methods are special methods in Python that start and
end with double underscores.

Examples:

    __init__
    __str__
    __eq__
    __lt__
    __gt__
    __add__

They are also called "dunder methods".

Dunder means:

    Double UNDERscore

For example:

    __str__

Python automatically calls these methods when we perform
certain operations on an object.

----------------------------------------------------------
WHY DO WE NEED MAGIC METHODS?
----------------------------------------------------------

Normally, Python does not automatically know how we want
our custom objects to behave.

For example:

    print(book1)

Python needs to know:

    "How should I display this Book object?"

We can tell Python how to handle it by creating:

    __str__()


Another example:

    book1 + book2

Python doesn't know what it means to add two Book objects.

We can define that behavior using:

    __add__()


So magic methods allow us to customize how our objects
behave with Python's built-in operations.


----------------------------------------------------------
1. __init__()
----------------------------------------------------------

__init__() is called automatically when we create an object.

Example:

    book1 = Book("Atomic Habits", "James Clear", 232)

Python automatically calls:

    __init__()

It is normally used to initialize the object's data.

In our example:

    self.title
    self.author
    self.num_pages

are created inside __init__().


----------------------------------------------------------
2. __str__()
----------------------------------------------------------

__str__() controls what happens when we use print()
with an object.

Example:

    print(book1)

Python automatically calls:

    book1.__str__()

Our method returns:

    "Atomic Habits by James Clear"

Without __str__(), Python would show something like:

    <__main__.Book object at 0x7fd430b93110>

So __str__() makes our objects easier to read.


----------------------------------------------------------
3. __eq__()
----------------------------------------------------------

__eq__() controls the == operator.

Example:

    book1 == book2

Python automatically calls:

    book1.__eq__(book2)

In our example, two books are considered equal when:

    title is the same
    AND
    author is the same

So we can decide what "equal" means for our objects.


----------------------------------------------------------
4. __lt__()
----------------------------------------------------------

__lt__() means "less than".

It controls the < operator.

Example:

    book1 < book2

Python automatically calls:

    book1.__lt__(book2)

In our example, we compare the number of pages.

So:

    book1 < book2

means:

    book1 has fewer pages than book2


----------------------------------------------------------
5. __gt__()
----------------------------------------------------------

__gt__() means "greater than".

It controls the > operator.

Example:

    book1 > book2

Python automatically calls:

    book1.__gt__(book2)

In our example, we compare the number of pages.

So:

    book1 > book2

means:

    book1 has more pages than book2


----------------------------------------------------------
6. __add__()
----------------------------------------------------------

__add__() controls the + operator.

Normally:

    10 + 20

means:

    30

But what should this mean?

    book1 + book2

Python doesn't automatically know.

So we define:

    __add__()

In our example:

    book1 + book2

adds the number of pages of both boovks.

For example:

    232 + 412

gives:

    644


----------------------------------------------------------
7. __contains__()
----------------------------------------------------------

__contains__() controls the "in" operator.

Example:

    "James" in book1

Python automatically calls:

    book1.__contains__("James")

Our method checks whether the keyword exists in:

    title
    OR
    author

For example:

    "James" in book1

returns:

    True


----------------------------------------------------------
8. __getitem__()
----------------------------------------------------------

__getitem__() controls the [] operator.

Normally, we use [] with lists and dictionaries.

Example:

    numbers[0]

or:

    student["name"]

We can also make our custom objects support [].

For example:

    book1["title"]

Python automatically calls:

    book1.__getitem__("title")

Our method returns:

    self.title

We can therefore write:

    book1["title"]
    book1["author"]
    book1["pages"]


----------------------------------------------------------
IMPORTANT IDEA
----------------------------------------------------------

We normally DON'T call magic methods directly.

Instead of:

    book1.__str__()

we normally write:

    print(book1)


Instead of:

    book1.__eq__(book2)

we normally write:

    book1 == book2


Instead of:

    book1.__lt__(book2)

we normally write:

    book1 < book2


Instead of:

    book1.__add__(book2)

we normally write:

    book1 + book2


Instead of:

    book1.__contains__("James")

we normally write:

    "James" in book1


Instead of:

    book1.__getitem__("title")

we normally write:

    book1["title"]


Python automatically calls the correct magic method.


----------------------------------------------------------
QUICK COMPARISON
----------------------------------------------------------

Operation              Magic Method
----------------------------------------------------------
Book(...)              __init__()
print(book)            __str__()
book1 == book2         __eq__()
book1 < book2          __lt__()
book1 > book2          __gt__()
book1 + book2          __add__()
"word" in book         __contains__()
book["title"]          __getitem__()


----------------------------------------------------------
EASY WAY TO REMEMBER
----------------------------------------------------------

Magic methods allow us to give normal Python operators
special behavior for our own objects.

For example:

    +       → __add__()
    ==      → __eq__()
    <       → __lt__()
    >       → __gt__()
    in      → __contains__()
    []      → __getitem__()
    print() → __str__()


The main idea is:

    Python operation
          ↓
    Magic method
          ↓
    Our custom behavior


Magic methods make custom objects behave more naturally
and work nicely with Python's built-in syntax.
"""