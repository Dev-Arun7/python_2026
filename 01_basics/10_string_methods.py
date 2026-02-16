"""
- Learn common string methods
- Understand how to modify and check strings
- Practice with simple examples

"""

# ----------------------------
# 1) Basic string
# ----------------------------
text = "  hello python world  "

print("Original text:", text)


# ----------------------------
# 2) upper() and lower()
# ----------------------------
print("\nUppercase:", text.upper())
print("Lowercase:", text.lower())


# ----------------------------
# 3) strip() - remove spaces
# ----------------------------
print("\nStripped text:", text.strip())


# ----------------------------
# 4) replace() - replace word with another
# ----------------------------
new_text = text.replace("python", "Arun")
print("\nReplace word:", new_text)


# ----------------------------
# 5) split() - split into list
# ----------------------------
words = text.strip().split(" ")
print("\nSplit into list:", words)


# ----------------------------
# 6) join() - join list into string
# ----------------------------
joined_text = "-".join(words)
print("\nJoined text:", joined_text)


# ----------------------------
# 7) find()
# ----------------------------
print("\nPosition of 'python':", text.find("python"))


# ----------------------------
# 8) startswith() and endswith()
# ----------------------------
clean_text = text.strip()

print("\nStarts with 'hello'?", clean_text.startswith("hello"))
print("Ends with 'world'?", clean_text.endswith("world"))


# ----------------------------
# 9) count()
# ----------------------------
sentence = "apple mango apple orange apple"

print("\nCount of 'apple':", sentence.count("apple"))


# ----------------------------
# 10) isalpha(), isdigit()
# ----------------------------
word = "Hello"
number = "12345"

print("\nIs 'Hello' only letters?", word.isalpha())
print("Is '12345' only digits?", number.isdigit())


# ----------------------------
# 11) capitalize() and title()
# ----------------------------
name = "arun balakrishnan"

print("\nCapitalize:", name.capitalize())
print("Title case:", name.title())


# ----------------------------
# 12) TODO Practice
# ----------------------------
# TODO:
# Create a variable city = "mumbai india"
# Print it in uppercase
# Replace "india" with "IN"
# Split into words

print("\nPractice string methods ✍️")

