"""
--------------------------------------------------
PASS STATEMENT IN PYTHON
--------------------------------------------------

The 'pass' statement does NOTHING.

It is used as a placeholder when:
- You need syntactically valid code
- You plan to implement logic later
- You intentionally want an empty block

Python requires an indented block after:
if, for, while, def, class, try, etc.
If you don't want to write code yet → use pass.
"""

# --------------------------------------------------
# Example 1: pass inside an if statement
# --------------------------------------------------

print("\nExample 1: pass inside if\n")

number = 10

if number > 0:
    pass  # TODO: Add logic later
else:
    print("Number is negative")


# --------------------------------------------------
# Example 2: pass inside a loop
# --------------------------------------------------

print("\nExample 2: pass inside loop\n")

for i in range(5):
    if i == 3:
        pass  # Nothing happens here
    print(i)

# Notice: pass does NOT skip the loop iteration.
# If you want to skip → use continue.


# --------------------------------------------------
# Example 3: pass vs continue (Important Difference)
# --------------------------------------------------

print("\nExample 3: pass vs continue\n")

print("Using pass:")
for i in range(5):
    if i == 2:
        pass
    print(i)

print("\nUsing continue:")
for i in range(5):
    if i == 2:
        continue
    print(i)



# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

"""
pass      → Does nothing (placeholder)
continue  → Skips current loop iteration
break     → Stops the loop completely
"""