"""
--------------------------------------------------
DICTIONARY IN PYTHON
--------------------------------------------------

Dictionary = Store data as key-value pairs

Rules:
- Keys must be unique
- Keys must be immutable (string, number, tuple)
- Values can be any type
- Values can repeat
"""

# --------------------------------------------------
# Creating Dictionaries
# --------------------------------------------------

# Dictionary with string keys and values
capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo"
}

# Dictionary with mixed value types
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Empty dictionary
student = {}

print("\nCapitals:", capitals)
print("Person:", person)
print("Student:", student)


# --------------------------------------------------
# Accessing Values (using get)
# --------------------------------------------------

print("\n--- Accessing Values ---")

value = capitals.get("France")
print("France:", value)

value_2 = capitals.get("Germany")  # key not present
print("Germany:", value_2)

value_3 = capitals.get("Germany", "Not Found")
print("Germany with default:", value_3)


# --------------------------------------------------
# Checking if Key Exists
# --------------------------------------------------

print("\n--- Checking Key ---")

if capitals.get("Germany") is None:
    print("Germany is NOT in dictionary")
else:
    print("Germany is in dictionary")


# --------------------------------------------------
# Adding New Key
# --------------------------------------------------

print("\n--- Adding Key ---")

capitals["Germany"] = "Berlin"
print(capitals)


# --------------------------------------------------
# Updating Value
# --------------------------------------------------

print("\n--- Updating Key ---")

capitals["USA"] = "Washington"
print(capitals)


# --------------------------------------------------
# Removing Items
# --------------------------------------------------

print("\n--- Removing Items ---")

# Remove specific key
capitals.pop("France")   # removed France
print("After pop France:", capitals)

# Remove last inserted item
capitals.popitem()   # removed Germany
print("After popitem:", capitals)


# --------------------------------------------------
# Clearing Dictionary
# --------------------------------------------------

print("\n--- Clearing Dictionary ---")

capitals.clear()
print("After clear:", capitals)