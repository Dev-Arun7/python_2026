# --------------------------------------------------
# FORMAT SPECIFIERS REFERENCE
# --------------------------------------------------

# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator

price_1 = 3.14159
price_2 = -987.53
price_3 = 12.7


# --------------------------------------------------
# 1️⃣ Control decimal places
# " .3f" → show 3 decimal places and add space for positive numbers
# " .1f" → show 1 decimal place
# --------------------------------------------------

print("DECIMAL FORMATTING\n")

print(f"Price 1 is ${price_1: .3f}")
print(f"Price 2 is ${price_2: .1f}")
print(f"Price 3 is ${price_3: .3f}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 2️⃣ Allocate width (10 spaces total)
# Numbers will be right aligned by default
# --------------------------------------------------

print("WIDTH ALLOCATION\n")

print(f"Price 1 is ${price_1: 10}")
print(f"Price 2 is ${price_2: 10}")
print(f"Price 3 is ${price_3: 10}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 3️⃣ Zero padding
# "010" → fill empty spaces with zeros
# --------------------------------------------------

print("ZERO PADDING\n")

print(f"Price 1 is ${price_1: 010}")
print(f"Price 2 is ${price_2: 010}")
print(f"Price 3 is ${price_3: 010}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 4️⃣ Left align within width
# "<10" → text starts from left
# --------------------------------------------------

print("LEFT ALIGN\n")

print(f"Price 1 is ${price_1: <10}")
print(f"Price 2 is ${price_2: <10}")
print(f"Price 3 is ${price_3: <10}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 5️⃣ Right align within width
# ">10" → text starts from right
# --------------------------------------------------

print("RIGHT ALIGN\n")

print(f"Price 1 is ${price_1: >10}")
print(f"Price 2 is ${price_2: >10}")
print(f"Price 3 is ${price_3: >10}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 6️⃣ Center align
# "^10" → value appears in center
# --------------------------------------------------

print("CENTER ALIGN\n")

print(f"Price 1 is ${price_1: ^10}")
print(f"Price 2 is ${price_2: ^10}")
print(f"Price 3 is ${price_3: ^10}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 7️⃣ Show sign (+)
# "+10" → always show + or -
# --------------------------------------------------

print("SHOW SIGN\n")

print(f"Price 1 is ${price_1:+10}")
print(f"Price 2 is ${price_2:+10}")
print(f"Price 3 is ${price_3:+10}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 8️⃣ Comma separator (commented example)
# Adds commas for thousands
# --------------------------------------------------

print(f"Price 1 is ${price_1: ,}")
print(f"Price 2 is ${price_2: ,}")
print(f"Price 3 is ${price_3: ,}")

print("\n----------------------------------------------\n")


# --------------------------------------------------
# 9️⃣ Combine multiple formatting
# "+,.f" → show sign + comma + round to nearest integer
# --------------------------------------------------

print("COMBINED FORMATTING\n")

print(f"Price 1 is ${price_1:+,.2f}")
print(f"Price 2 is ${price_2:+,.2f}")
print(f"Price 3 is ${price_3:+,.2f}")


print("\n----------------------------------------------\n")