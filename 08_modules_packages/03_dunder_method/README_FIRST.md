# 📘 Understanding __name__ and Dunder Methods in Python

---

## 1️⃣ What is a Dunder Method?

"Dunder" means:

Double + Under

It refers to names that have double underscores:

Example:

__name__  
__init__  
__str__  

They look like this:

__something__

These are **special built-in variables or methods** in Python.

---

## 2️⃣ What is __name__ ?

__name__ is a special built-in variable.

Python automatically creates it.

It tells us:

👉 How this file is being used.

---

## 3️⃣ Two Possible Values of __name__

### Case 1: When you RUN a file directly

Example:

python script_1.py

Then inside that file:

__name__ == "__main__"

Meaning:

"This file is the main program."

---

### Case 2: When you IMPORT a file

Example:

import script_2

Then inside script_2:

__name__ == "script_2"

Meaning:

"This file is being used as a module."

---

## 4️⃣ Why Do We Use This?

We write this:

if __name__ == "__main__":
    main()

It means:

"Run this code ONLY if this file is executed directly."

It prevents automatic execution when importing.

---

## 5️⃣ Simple Example

### script_2.py

```python
def hello():
    print("Hello from script_2")

if __name__ == "__main__":
    print("Running directly")
    hello()

print("File loaded")