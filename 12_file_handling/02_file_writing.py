"""
Writing Text to a File

open() is used to open a file.

Common modes:

    "w" = Write
    "a" = Append
    "x" = Create a new file
    "r" = Read
"""


txt_data = "I love Python!"

file_path = "/home/arun/Documents/python_2026/12_file_handling/out.txt"


# "w" mode opens the file for writing.
# If the file doesn't exist, Python creates it.
# If the file already exists, its old content is replaced.
with open(file=file_path, mode="w") as file:

    file.write(txt_data)

    print(f"Text file '{file_path}' was created")


"""
FILE MODES
----------

"w" = Write
----------------
Writes data to the file.

If the file doesn't exist:
    → Creates the file

If the file already exists:
    → Deletes the old content and writes the new content


"a" = Append
----------------
Adds new data to the end of the file.

If the file doesn't exist:
    → Creates the file

If the file already exists:
    → Keeps the old content and adds new content at the end


"x" = Create
----------------
Creates a new file.

If the file doesn't exist:
    → Creates the file

If the file already exists:
    → Gives an error


"r" = Read
----------------
Opens the file for reading.

If the file doesn't exist:
    → Gives an error


Quick memory:

    "r" → Read
    "w" → Write
    "a" → Append
    "x" → Create


Example:

    with open("out.txt", "w") as file:
        file.write("Hello")


The 'with' statement automatically closes the file
after we finish working with it.
"""