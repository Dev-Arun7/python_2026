"""
File and Directory Detection

Python's os.path module provides useful functions to check
whether a file or directory exists.

    os.path.exists()  -> Checks if the path exists
    os.path.isfile()  -> Checks if the path is a file
    os.path.isdir()   -> Checks if the path is a directory

These functions return either True or False.
"""


import os


# File path
file_path = "home/the_file.txt" # change it based on your file path


# Check whether the path exists
if os.path.exists(file_path):
    print(f"'{file_path}' exists")
else:
    print(f"'{file_path}' doesn't exist")


# Check whether the path is a file
if os.path.isfile(file_path):
    print(f"'{file_path}' is a file")
else:
    print(f"'{file_path}' is not a file")


# Check whether the path is a directory
if os.path.isdir(file_path):
    print(f"'{file_path}' is a directory")
else:
    print(f"'{file_path}' is not a directory")


# Directory path
directory_path = "home/test_folder" # change it based on your folder structure


# Check whether the directory exists
if os.path.exists(directory_path):
    print(f"'{directory_path}' exists")
else:
    print(f"'{directory_path}' doesn't exist")


# Check whether the path is a directory
if os.path.isdir(directory_path):
    print(f"'{directory_path}' is a directory")
else:
    print(f"'{directory_path}' is not a directory")


"""
IMPORTANT DIFFERENCE
--------------------

os.path.exists()
    ↓
Checks whether the path exists.

    File      → True
    Directory → True
    Nothing   → False


os.path.isfile()
    ↓
Checks whether the path is a file.

    File      → True
    Directory → False
    Nothing   → False


os.path.isdir()
    ↓
Checks whether the path is a directory.

    File      → False
    Directory → True
    Nothing   → False


Example:

If we have:

    12_file_handling/
    ├── the_file.txt
    └── test_folder/


For:

    os.path.exists("the_file.txt")
    → True

    os.path.isfile("the_file.txt")
    → True

    os.path.isdir("the_file.txt")
    → False


For:

    os.path.exists("test_folder")
    → True

    os.path.isfile("test_folder")
    → False

    os.path.isdir("test_folder")
    → True


Simple way to remember:

    exists()
        ↓
    "Does it exist?"


    isfile()
        ↓
    "Is it a file?"


    isdir()
        ↓
    "Is it a directory?"


Relative and absolute paths
---------------------------

Relative path:

    "the_file.txt"

Python looks for it in the current working directory.


Absolute path:

    "/home/arun/Documents/python_2026/12_file_handling/the_file.txt"

This gives the complete location of the file.

The current working directory can be checked with:

    os.getcwd()
"""