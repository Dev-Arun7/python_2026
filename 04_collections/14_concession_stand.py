"""
A simple concession stand program.
User selects items from menu.
Program calculates total cost.
"""

# ----------------------------------------
# Menu (dictionary: item -> price)
# ----------------------------------------

menu = {
    "hot dog": 2.50,
    "burger": 3.50,
    "fries": 1.50,
    "soda": 1.00,
    "popcorn": 5.00,
    "candy": 2.00,
    "nachos": 4.00
}

cart = []          # List to store selected items
total_cost = 0.0   # Variable to store total cost

# ----------------------------------------
# Display Menu
# ----------------------------------------

print("Welcome to the Concession Stand! 🍔")
print("\n----------- MENU -----------")

for item, price in menu.items():
    print(f"{item:10} : ${price:.2f}")

print("-----------------------------")

# ----------------------------------------
# Take User Orders
# ----------------------------------------

while True:
    food = input("Enter item name (Q to quit): ").lower()

    if food == "q":
        break

    elif food in menu:
        cart.append(food)

    else:
        print("Item not found ❌ Try again.")


# ----------------------------------------
# Calculate Total Cost
# ----------------------------------------

# Finding the total
for item in cart:
    total_cost += menu[item]   


# ----------------------------------------
# Show Cart
# ----------------------------------------

print("\n----------- YOUR CART -----------")

if len(cart) == 0:
    print("Your cart is empty.")
else:
    for item in cart:
        print(f"{item:10} : ${menu[item]:.2f}")

    print("-------------------------------")
    print(f"Total Cost : ${total_cost:.2f}")

print("\nThank you! 😊")