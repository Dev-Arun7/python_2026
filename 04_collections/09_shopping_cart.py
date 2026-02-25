"""
Here we're going to make a shopping cart using all the collections we've learned so far.
"""

foods = []   # Using list to store foods (ordered, duplicates allowed)
prices = []  # Using list to store prices
total = 0    # Using int to store total price

while True:
    food = input("Enter food name (Q to quit): ")

    if food.upper() == "Q":
        break
    else:
        price = float(input(f"Enter price for {food}: "))  

        foods.append(food)   
        prices.append(price)

        total += price

print("\n----------- YOUR CART -----------")

# Print foods with price
for i in range(len(foods)):
    print(f"{foods[i]} - ${prices[i]:.2f}")

print("-------------------------------")
print(f"Total: ${total:.2f}")