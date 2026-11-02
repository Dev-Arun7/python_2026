
"""
Learning: OOP Mini Project - Shopping Cart

In this project, we are building a simple shopping
cart and payment system.

A customer can:

    - View product details.
    - Add products to the cart.
    - Calculate the total price.
    - Make a payment.
    - View the order receipt.


Classes used:

    Product
    Customer
    Order
    Payment
    UPIPayment
    CardPayment


OOP concepts used:

    - Classes and Objects
    - Constructors
    - Composition
    - Encapsulation
    - Inheritance
    - Abstraction
    - Polymorphism

The main idea is to make different classes
work together to build a small application.
"""

from abc import ABC, abstractmethod
# ---------------------------------------------------
# Product Class
# ---------------------------------------------------

class Product:

    def __init__(self, name, price):

        # Store product information
        self.name = name
        self.price = price

    # Display product details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Price: ${self.price}")


# ---------------------------------------------------
# Customer Class
# ---------------------------------------------------

class Customer:

    def __init__(self, name, email):

        # Store customer information
        self.name = name
        self.email = email

    # Display customer details
    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")


# ---------------------------------------------------
# Order Class
# ---------------------------------------------------

class Order:

    def __init__(self, customer):

        # Store the Customer object inside the Order
        self.customer = customer

        # Store all products added to the cart
        self.products = []

        # Initial order status
        self.status = "Pending"

    # Add a product to the cart
    def add_product(self, product):

        # Add the Product object to the products list
        self.products.append(product)

        print(f"{product.name} added to your cart")

    # Display all products in the cart
    def show_order(self):

        print("-------Your cart-------")

        # enumerate() gives both the index and product
        # start=1 makes the numbering begin from 1
        for i, product in enumerate(self.products, start=1):
            print(f"{i}: {product.name} - ${product.price}")

    # Calculate the total price of all products
    def calculate_total(self):

        total = 0

        for product in self.products:
            total += product.price

        return total

    # Process payment for the order
    def make_payment(self, payment):

        # Do not allow payment for an empty cart
        if not self.products:
            print("Your cart is empty, add some products first")
            return

        # Call the pay() method of the payment object
        if payment.pay():

            # Update order status only if payment succeeds
            self.status = "Paid"

    # Display the final order receipt
    def show_receipt(self):

        print("========== ORDER RECEIPT ==========")

        # Customer details
        print(f"Customer: {self.customer.name}")
        print(f"Email: {self.customer.email}")

        print("")
        print("Products:  ")

        # Display all purchased products
        for i, product in enumerate(self.products, start=1):
            print(f"{i}: {product.name} - ${product.price}")

        print()

        # Calculate and display the total price
        total = self.calculate_total()

        print(f"Total: {total}")
        print(f"Payment Status: {self.status}")

        print("===================================")


# ---------------------------------------------------
# Abstract Payment Class
# ---------------------------------------------------

class Payment(ABC):

    # Every payment method must implement pay()
    @abstractmethod
    def pay(self):
        pass


# ---------------------------------------------------
# UPI Payment Class
# ---------------------------------------------------

# Inherits from Payment
class UPIPayment(Payment):

    def __init__(self, amount):

        self.amount = amount

    # Implement the abstract pay() method
    def pay(self):

        if self.amount <= 0:
            print("Payment failed...!")
            return False

        print(f"UPI payment successful: ${self.amount}")

        # Return True to indicate successful payment
        return True


# ---------------------------------------------------
# Card Payment Class
# ---------------------------------------------------

# Also inherits from Payment
class CardPayment(Payment):

    def __init__(self, amount):

        self.amount = amount

    # Implement the abstract pay() method
    def pay(self):

        if self.amount <= 0:
            print("Payment failed...!")
            return False

        print(f"Card payment successful: ${self.amount}")

        # Return True to indicate successful payment
        return True


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Create a Customer object
customer1 = Customer("Arun", "arun@gmail.com")

# Create Product objects
product1 = Product("mouse", 99)
product2 = Product("keyboard", 120)

# Create an Order object and pass the Customer object
order1 = Order(customer1)


# ---------------------------------------------------
# Shopping Cart Operations
# ---------------------------------------------------

# Add products to the cart
order1.add_product(product1)
order1.add_product(product2)

# Display cart contents
order1.show_order()

# Calculate the total price
total = order1.calculate_total()


# ---------------------------------------------------
# Payment
# ---------------------------------------------------

# Create a CardPayment object using the total amount
payment = CardPayment(total)

# Pass the payment object to the Order
order1.make_payment(payment)


# ---------------------------------------------------
# Order Receipt
# ---------------------------------------------------

print(f"Order status: {order1.status}")

# Display the final receipt
order1.show_receipt()


"""
===================================================
SHORT NOTE: OOP CONCEPTS USED
===================================================

1. Classes and Objects
   Product, Customer, Order and Payment are classes.
   We create objects from these classes.

2. Composition
   Order contains a Customer object and a list
   of Product objects.

3. Inheritance
   UPIPayment and CardPayment inherit from Payment.

4. Abstraction
   Payment defines the abstract pay() method.

5. Polymorphism
   Both payment classes implement pay() differently.
   Order can call payment.pay() without knowing
   which payment method is being used.

6. Encapsulation
   Each class keeps related data and methods together.

7. Object Interaction
   Order communicates with Customer, Product
   and Payment objects.

8. enumerate()
   Used to display products with numbering.


MAIN IDEA
---------

A real application is built by connecting different
classes and objects.

Each class handles its own responsibility.

Together, they form a complete working system.
"""
