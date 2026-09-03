"""
Reading Data from Files

We can read different types of files using Python:

    Text file → open() + read()
    JSON file → json.load()
    CSV file → csv.reader()

We can also use try/except to handle common file errors,
such as a missing file or permission problems.
"""


# ===========================================================
# ---------- Reading a Text File ----------------------------
# ===========================================================

file_path = "/home/arun/Documents/python_2026/12_file_handling/the_file.txt"

try:

    # "r" mode opens the file for reading.
    with open(file_path, "r") as file:

        # read() reads the entire file.
        content = file.read()

        print(content)

except FileNotFoundError:

    print("That file was not found!")

except PermissionError:

    print("You do not have permission to read the file!")


# ===========================================================
# ---------- Reading a JSON File ----------------------------
# ===========================================================

import json


file_path = "/home/arun/Documents/python_2026/12_file_handling/json_out.json"

try:

    with open(file_path, "r") as file:

        # json.load() reads the JSON file
        # and converts it into a Python object.
        content = json.load(file)

        print(content)

        # JSON object is converted into a Python dictionary,
        # so we can access its values using a key.
        print(content["name"])

except FileNotFoundError:

    print("That file was not found!")

except PermissionError:

    print("You do not have permission to read the file!")


# ===========================================================
# ---------- Reading a CSV File -----------------------------
# ===========================================================

import csv


file_path = "/home/arun/Documents/python_2026/12_file_handling/csv_out.csv"

try:

    with open(file_path, "r") as file:

        # csv.reader() reads the CSV file row by row.
        content = csv.reader(file)

        for line in content:
            print(line)

except FileNotFoundError:

    print("That file was not found!")

except PermissionError:

    print("You do not have permission to read the file!")


"""
IMPORTANT
---------

Text file:
    read() → Reads the file as text.

JSON file:
    json.load() → Reads JSON and converts it into
                  a Python dictionary/list.

CSV file:
    csv.reader() → Reads the CSV file row by row.


COMMON FILE ERRORS
------------------

FileNotFoundError
    → The specified file does not exist.

PermissionError
    → Python does not have permission to access the file.


Simple flow:

    try
      ↓
    Open file
      ↓
    Read file
      ↓
    If an error happens
      ↓
    except handles the error
"""