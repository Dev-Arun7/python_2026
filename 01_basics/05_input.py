# Input function allows us to get user input from the console.
# The input function always returns a string, so we may need to convert it to the appropriate type if we want to perform operations on it.
# Example: Get user's name and age, then print a greeting message.



name = input("What is your name? ")
age = input("How old are you? ")

# Convert age to an integer (optional, but useful if we want to do math with it)
age = int(age)
print(f"Hello, {name}! You are {age} years old.")



# Another example: Find the area of a rectangle given its width and height from user input.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}cm^2")


# Example:  Shoping cart program
item  = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity you want to buy: "))
total_cost = price * quantity
print(f"You want to buy {quantity} {item}(s) for a total of ${total_cost:.2f}.") # :.2f formats the total cost to 2 decimal places