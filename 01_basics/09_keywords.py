"""
- Understand what keywords are
- Learn how to see all Python keywords
- Learn why keywords cannot be used as variable names
"""

# ----------------------------
# 1) What are keywords?
# ----------------------------
# Keywords are reserved words in Python.
# They have special meaning and cannot be used as variable names.

print("Python keywords are reserved words 🙂")


# ----------------------------
# 2) View all keywords
# ----------------------------
# Python provides a built-in module called keyword

import keyword

print("\nList of Python keywords:")
print(keyword.kwlist)


# ----------------------------
# 3) Count total keywords
# ----------------------------
print("\nTotal number of keywords:", len(keyword.kwlist))


# ----------------------------
# 4) Why keywords cannot be used as variable names
# ----------------------------
# Uncomment below lines one by one to see errors

# if = 10
# class = "Python"
# for = 5

print("\nKeywords cannot be used as variable names ❌")


# ----------------------------
# 5) Correct variable naming
# ----------------------------
# Use meaningful names instead

if_value = 10
class_name = "Python"
for_count = 5

print("if_value =", if_value)
print("class_name =", class_name)
print("for_count =", for_count)


# ----------------------------
# 6) Check if a word is keyword
# ----------------------------
word1 = "for"
word2 = "hello"

print("\nIs 'for' a keyword?", keyword.iskeyword(word1))
print("Is 'hello' a keyword?", keyword.iskeyword(word2))


# ----------------------------
# 7) TODO Practice
# ----------------------------
# TODO: Check if 'while' is a keyword using keyword.iskeyword()

print("\nPractice checking keywords ✍️")

