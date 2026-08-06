# simple wright convertor that converts weight from kilograms to pounds and vice versa based on user input.

# Get user input for weight
weight = float(input("Enter the weight: "))
unit = input("Enter the unit (kg for kilograms, lb for pounds): ").lower()  # Convert the unit to lowercase for consistency

# Perform the conversion based on the unit
if unit == 'kg':
    converted_weight = round(weight * 2.20462, 2)  # Convert kg to lb
    print(f"{weight} kg is equal to {converted_weight} lb.")
elif unit == 'lb':
    converted_weight = round(weight / 2.20462, 2)  # Convert lb to kg
    print(f"{weight} lb is equal to {converted_weight} kg.")
else:
    print(f"Error: Invalid unit '{unit}'....!")