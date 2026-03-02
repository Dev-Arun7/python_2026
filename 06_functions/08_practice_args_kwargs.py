"""
--------------------------------------------------
Using *args and **kwargs in One Function
--------------------------------------------------

*args   → collects multiple positional arguments (tuple)
**kwargs → collects multiple keyword arguments (dictionary)
"""

# --------------------------------------------------
# Function Definition
# --------------------------------------------------

def person(*args, **kwargs):

    # -----------------------------
    # 1️⃣ Print Full Name (*args)
    # -----------------------------
    print("Full Name:")
    for arg in args:
        print(arg, end=" ")
    print()   # move to next line


    # -----------------------------
    # 2️⃣ Print All Details (**kwargs)
    # -----------------------------
    print("\nAll Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}", end=", ")
    print("\n" + "-" * 60)


    # -----------------------------
    # 3️⃣ Conditional Printing
    # -----------------------------
    print("Formatted Address:")

    if "flat_no" in kwargs:
        print(f"{kwargs.get('house')}, {kwargs.get('flat_no')}")
    else:
        print(f"{kwargs.get('house')}")

    print(f"{kwargs.get('place')}")
    print(f"{kwargs.get('state')}, PIN Code: {kwargs.get('pin')}")
    print("\n" + "=" * 60 + "\n")


# --------------------------------------------------
# 1️⃣ First Call (No flat number)
# --------------------------------------------------

person(
    "Arun", "Balakrishnan",
    place="Iritty",
    house="B12",
    state="Kerala",
    pin=670703
)


# --------------------------------------------------
# 2️⃣ Second Call (With flat number)
# --------------------------------------------------

person(
    "Dr", "Anila", "VR",
    place="Kochi",
    house="Green Villa",
    flat_no="12A",
    state="Kerala",
    pin=682001
)