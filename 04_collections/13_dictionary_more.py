"""
--------------------------------------------------
MORE DICTIONARY METHODS
--------------------------------------------------
"""

# --------------------------------------------------
# Create Dictionary
# --------------------------------------------------

capitals = {
    "USA": "Washington D.C.",
    "France": "Paris",
    "Japan": "Tokyo",
    "India": "New Delhi"
}

print("Dictionary:", capitals)


# --------------------------------------------------
# Get All Keys
# --------------------------------------------------

print("\n--- Keys ---")

all_keys = capitals.keys()
print("Keys object:", all_keys)

# Loop through keys
for k in capitals.keys():
    print(k)


# --------------------------------------------------
# Get All Values
# --------------------------------------------------

print("\n--- Values ---")

all_values = capitals.values()
print("Values object:", all_values)

# Loop through values
for v in capitals.values():
    print(v)


# --------------------------------------------------
# Get All Items (Key + Value)
# --------------------------------------------------

print("\n--- Items ---")

all_items = capitals.items()
print("Items object:", all_items)

# Loop through items
for key, value in capitals.items():
    print(f"key: {key}, value: {value}")


# --------------------------------------------------
# Check if Key Exists
# --------------------------------------------------

print("\n--- Check Key ---")

if "India" in capitals:
    print("India exists in dictionary")


# --------------------------------------------------
# Get Length
# --------------------------------------------------

print("\n--- Length ---")

print("Total items:", len(capitals))


# --------------------------------------------------
# Copy Dictionary
# --------------------------------------------------

print("\n--- Copy ---")

copy_dict = capitals.copy()
print("Copy:", copy_dict)


# --------------------------------------------------
# Update Dictionary
# --------------------------------------------------

print("\n--- Update ---")

capitals.update({"Germany": "Berlin"})
print("After update:", capitals)