"""
Generator Example: Reading a File

A generator can be used to read a file one line at a time.

This is useful for large files because we don't need to load
the entire file into memory at once.
"""


def read_file(file_path):

    with open(file_path) as file:

        for line in file:

            yield line.strip()  # Produce one line at a time


file_path = "/home/arun/Documents/python_2026/014_other_concepts/test.txt" # Change path for your file

for line in read_file(file_path):

    print(line)


"""
HOW IT WORKS
------------
read_file() is a generator function because it uses yield.

Instead of reading the entire file at once:

    file.read()

we read one line at a time:

    for line in file:

        yield line.strip()


When the for loop asks for the next value:

    yield

produces the next line and pauses the generator.


MEMORY
------
For a small file, reading the entire file is usually fine.

For a large file:

    10 GB file
        ↓
    Don't load everything into memory
        ↓
    Read one line
        ↓
    Process it
        ↓
    Read next line
        ↓
    ...


IMPORTANT
---------
This:

    yield line.strip()

does two things:

    line.strip()
        Removes spaces and the newline character.

    yield
        Produces the line and pauses the generator.


Simple idea:

    File
      ↓
    One line
      ↓
    yield
      ↓
    One line
      ↓
    yield
      ↓
    ...


This is one of the practical uses of generators.
"""