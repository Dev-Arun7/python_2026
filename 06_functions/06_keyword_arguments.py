"""
--------------------------------------------------
KEYWORD ARGUMENTS IN PYTHON
--------------------------------------------------

Keyword Argument:
An argument that is passed using parameter_name = value

Advantages:
- Improves readability
- Order does NOT matter
- Reduces mistakes when many parameters exist
"""
# --------------------------------------------------
# Function Definition
# --------------------------------------------------

def greeting(message, title, first_name, last_name):
    print(f"{message} {title} {first_name} {last_name}, how are you?")

# --------------------------------------------------
# Variables
# --------------------------------------------------

msg = "Hi"
title = "Mr"
first = "Arun"
last = "Balakrishnan"

# --------------------------------------------------
# 1️⃣ Positional Arguments (Order MUST be correct)
# --------------------------------------------------

print("\n--- Positional Arguments (Correct Order) ---")
greeting(msg, title, first, last)   # ✅ Correct order

print("\n--- Positional Arguments (Wrong Order) ---")
greeting(first, last, title, msg)   # ❌ Order changed → Output becomes wrong


# --------------------------------------------------
# 2️⃣ Keyword Arguments (Order does NOT matter)
# --------------------------------------------------

print("\n--- Keyword Arguments (Any Order) ---")
greeting(first_name=first, last_name=last, title=title, message=msg)   # ✅ Order doesn't matter


# --------------------------------------------------
# 3️⃣ Mixing Positional and Keyword Arguments
# --------------------------------------------------

print("\n--- Mixing Positional and Keyword ---")
greeting("Hello",
         title=title,
         first_name=first,
         last_name=last)   # ✅ Works

# ⚠️ Important Rule:
# Positional arguments must come BEFORE keyword arguments
# This is wrong and will give error:
#
# greeting(message="Hi", title, first_name=first, last_name=last)
# -----------------------------------------------
# SyntaxError: positional argument follows keyword argument