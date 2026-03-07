"""
--------------------------------------------------
MODULE IN PYTHON
--------------------------------------------------

Module = A file that contains Python code
         (functions, variables, classes)

We use 'import' to include a module.

Modules help:
- Break large programs into small parts
- Reuse code
- Keep code organized
"""

# --------------------------------------------------
# 1️⃣ Importing Full Module
# --------------------------------------------------

import math

print("Using math module:")
print("Square root of 16:", math.sqrt(16))
print("Power 2^3:", math.pow(2, 3))
print("Value of Pi:", math.pi)


print("\n" + "-" * 60)


# --------------------------------------------------
# 2️⃣ Import with Alias
# --------------------------------------------------

import math as m

print("Using alias 'm':")
print("Square root of 25:", m.sqrt(25))


print("\n" + "-" * 60)


# --------------------------------------------------
# 3️⃣ Import Specific Item
# --------------------------------------------------

from math import pi

print("Importing only pi:")
print("Value of Pi:", pi)


print("\n" + "-" * 60)


# --------------------------------------------------
# 4️⃣ Random Module
# --------------------------------------------------

import random

print("Random Module Example:")
print("Random number (0 to 1):", random.random())
print("Random integer (1 to 10):", random.randint(1, 10))


print("\n" + "-" * 60)


# --------------------------------------------------
# 5️⃣ Datetime Module
# --------------------------------------------------

import datetime

today = datetime.datetime.now()

print("Datetime Module Example:")
print("Current Date and Time:", today)


print("\n" + "-" * 60)


# --------------------------------------------------
# 6️⃣ OS Module
# --------------------------------------------------

import os

# --------------------------------------------------
# 1️⃣ Current Working Directory
# --------------------------------------------------

print("Current Working Directory:")
print(os.getcwd())


print("\n" + "-" * 60)


# --------------------------------------------------
# 2️⃣ List Files and Folders
# --------------------------------------------------

print("Files and Folders in Current Directory:")
files = os.listdir()

for file in files:
    print(file)


print("\n" + "-" * 60)


# --------------------------------------------------
# 3️⃣ Create a New Folder
# --------------------------------------------------

folder_name = "test_folder"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")


print("\n" + "-" * 60)


# --------------------------------------------------
# 4️⃣ Check if File or Folder Exists
# --------------------------------------------------

print("Does 'test_folder' exist?")
print(os.path.exists("test_folder"))


print("\n" + "-" * 60)


# --------------------------------------------------
# 5️⃣ Get Absolute Path
# --------------------------------------------------

file_name = "test_folder"
print("Absolute Path:")
print(os.path.abspath(file_name))


print("\n" + "-" * 60)


# --------------------------------------------------
# 6️⃣ Remove Folder (Be Careful ⚠️)
# --------------------------------------------------

# This works only if folder is empty
# Uncomment to test carefully

# os.rmdir("test_folder")
# print("Folder removed.")


print("\nProgram Finished ✅")