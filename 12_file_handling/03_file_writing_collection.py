"""
Writing Data from Collections to Files

We can write data from Python collections such as:

    List       → Text file
    Dictionary → JSON file
    List       → CSV file
"""


# ===========================================================
# ---------- Writing a List into a Text File ----------------
# ===========================================================

employees = ["Tom", "Simba", "Rio", "Patric"]

file_path = "/home/arun/Documents/python_2026/12_file_handling/out.txt"


# "w" mode opens the file for writing.
# If the file doesn't exist, Python creates it.
# If the file already exists, its old content is replaced.
with open(file=file_path, mode="w") as file:

    for employee in employees:
        file.write(employee + "    ")

    print(f"Text file '{file_path}' was created")


# ===========================================================
# ---------- Writing a Dictionary into JSON ----------------
# ===========================================================

import json


data = {
    "name": "Arun",
    "age": 33,
    "job": "cook"
}

file_path = "/home/arun/Documents/python_2026/12_file_handling/json_out.json"


with open(file=file_path, mode="w") as file:

    # json.dump() converts the Python dictionary into JSON
    # and writes it directly into the file.
    json.dump(data, file)

    print(f"JSON file '{file_path}' was created")


# ===========================================================
# ---------- Writing a List into CSV ------------------------
# ===========================================================

import csv


workers = [
    ["Name", "Age", "Job"],
    ["Arun", 33, "unemployed"],
    ["Akhil", 28, "cook"],
    ["Simba", 38, "Scientist"]
]

file_path = "/home/arun/Documents/python_2026/12_file_handling/csv_out.csv"


with open(file=file_path, mode="w") as file:

    # Create a CSV writer object.
    writer = csv.writer(file)

    # Write each list as a row in the CSV file.
    for row in workers:
        writer.writerow(row)

    print(f"CSV file '{file_path}' was created")