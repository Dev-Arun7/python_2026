"""
--------------------------------------------------
*args and **kwargs IN PYTHON
--------------------------------------------------

*args   → Allows passing multiple NON-keyword arguments
          (collected as a tuple)

**kwargs → Allows passing multiple KEYWORD arguments
           (collected as a dictionary)

kwargs = keyword arguments
Inside the function, **kwargs becomes a dictionary.
So we get key-value pairs.
"""
# --------------------------------------------------
# 1️⃣ Traditional Function (Fixed parameters)
# --------------------------------------------------

def address(place, city, pin):
    print(f"Place is {place}")
    print(f"City is {city}")
    print(f"PIN code is {pin}")


print("Traditional function:")
address("Padiyur", "Kannur", 670123)

# ❌ If we want to add state or country,
# we must change the function definition.
# So it is not flexible.


print("\n" + "-" * 60)


# --------------------------------------------------
# 2️⃣ Using **kwargs (Flexible keyword arguments)
# --------------------------------------------------

def address_2(**kwargs):
    # kwargs is a dictionary
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("Using **kwargs:")
address_2(place="Padiyur", city="Calicut", state="Kerala", country="India", pin=123654)


print("\n" + "-" * 60)


# ---------------------------------------------------------------------
# 3️⃣ Calling again with different data , another style , more readable
# ---------------------------------------------------------------------

print("Calling with different keys:")
address_2(
    name="Arun",
    flat="12B",
    state="MH",
    pin=400706
)