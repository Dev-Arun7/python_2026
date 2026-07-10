"""
--------------------------------------------------
TYPE HINTS IN PYTHON (Complete Example Script)
--------------------------------------------------

Type hints tell:
- What type of data a function expects
- What type it returns

They improve readability and help IDEs.
They DO NOT enforce types at runtime.
"""

from typing import Union, List, Dict


# --------------------------------------------------
# 1️⃣ Basic Type Hint
# --------------------------------------------------

def add_numbers(a: int, b: int) -> int:
    """Adds two integers and returns an integer."""  # Doc string
    return a + b


print("Basic Type Hint:")
print(add_numbers(10, 5))


# --------------------------------------------------
# 2️⃣ Multiple Possible Types (Union)
# --------------------------------------------------

def add_values(a: Union[int, float], b: Union[int, float]) -> float:
    """Adds int or float values."""
    return a + b


print("\nUnion Example:")
print(add_values(5, 2.5))


# --------------------------------------------------
# 3️⃣ List Type Hint
# --------------------------------------------------

def total_numbers(numbers: List[int]) -> int:
    """Returns total of a list of integers."""
    total = 0
    for num in numbers:
        total += num
    return total


print("\nList Example:")
print(total_numbers([1, 2, 3, 4]))


# --------------------------------------------------
# 4️⃣ Dictionary Type Hint
# --------------------------------------------------

def print_data(data: Dict[str, int]) -> None:
    """Prints dictionary with string keys and integer values."""
    for key, value in data.items():
        print(f"{key}: {value}")


print("\nDictionary Example:")
print_data({"age": 25, "year": 2026})


# --------------------------------------------------
# 5️⃣ Type Hint with *args
# --------------------------------------------------

def show_numbers(*args: int) -> None:
    """Prints multiple integer values."""
    for num in args:
        print(num)


print("\n*args Example:")
show_numbers(1, 2, 3)


# --------------------------------------------------
# 6️⃣ Type Hint with **kwargs
# --------------------------------------------------

def show_info(**kwargs: str) -> None:
    """Prints keyword arguments (string values)."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print("\n**kwargs Example:")
show_info(name="Arun", city="Kannur")