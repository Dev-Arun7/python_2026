"""
====================================================
              DEFAULT ARGUMENTS 
====================================================

Default Argument = A value that is already given
inside the function.

If we don't send a value while calling the function,
Python will use the default value.

But if we send a value,
it will override (replace) the default value.
"""
# ====================================================
# Example: Calculate Final Bill with Delivery Charge
# ====================================================

def calculate_bill(price, delivery_charge=50, tax_percent=5):

    # Convert tax percent to actual tax amount
    tax_amount = price * (tax_percent / 100)

    # Final total
    total = price + delivery_charge + tax_amount

    return total


# ====================================================
# 1️⃣ Calling with ONLY required argument
# ====================================================

# Here:
# price = 1000
# delivery_charge = 50 (default value used)
# tax_percent = 5 (default value used)

bill_1 = calculate_bill(1000)
print("Bill 1:", bill_1)


# ====================================================
# 2️⃣ Overriding default values
# ====================================================

# Here we change delivery_charge and tax_percent,
# We provide the value

bill_2 = calculate_bill(1000, 100, 10)
print("Bill 2:", bill_2)


# ====================================================
# 3️⃣ Changing only one default value
# ====================================================

# Here:
# price = 1000
# delivery_charge = 0 (we changed it)
# tax_percent = 5 (default still used)

bill_3 = calculate_bill(1000, 0)
print("Bill 3:", bill_3)




# ====================================================
# IMPORTANT RULE
# ====================================================
# 1. Parameters with default values must come AFTER
#    normal parameters.
#
#    Correct:
#       def test(a, b=10):
#
#    Wrong:
#       def test(a=10, b):
#
# 2. Default value is used ONLY if we don't pass value.
#
# 3. If we pass a value, default is ignored.
#
# ====================================================
# Think like this:
#
# Function = Machine
# Default argument = Pre-set setting in machine
#
# If you don't change the setting,
# machine uses default setting.
#
# If you change it,
# machine uses your new setting.
# ====================================================