
"""
Learning: Abstraction

Abstraction means:

    "Hiding unnecessary internal details and showing
     only what is needed to use something."

In this example, we have different payment methods:

    UPI Payment
    Card Payment

Both payment methods have a common method:

    pay()

But each payment method handles the payment
in its own way.


        Payment
        /     \
       /       \
      ↓         ↓
   UPI       Card
  Payment   Payment


The important part is:

    @abstractmethod

It tells child classes that they must implement
the abstract method defined by the parent class.
"""


# ---------------------------------------------------
# Importing Abstract Class Tools
# ---------------------------------------------------

# ABC: Used to create an Abstract Base Class.
# abstractmethod: Used to define methods that child
# classes must implement.

from abc import ABC, abstractmethod


# ---------------------------------------------------
# Parent Abstract Class
# ---------------------------------------------------

class Payment(ABC):

    # Abstract method
    # Every child class must provide its own pay() method.
    @abstractmethod
    def pay(self):
        pass


# ---------------------------------------------------
# UPI Payment Class
# ---------------------------------------------------

# UPIPayment inherits from Payment
class UPIPayment(Payment):

    # Constructor
    def __init__(self, amount):

        # Store the payment amount
        self.amount = amount

    # Implementation of the abstract pay() method
    def pay(self):

        # UPI-specific payment message
        print(f"UPI payment successful: ₹{self.amount}")


# ---------------------------------------------------
# Card Payment Class
# ---------------------------------------------------

# CardPayment also inherits from Payment
class CardPayment(Payment):

    # Constructor
    def __init__(self, amount):

        # Store the payment amount
        self.amount = amount

    # Implementation of the abstract pay() method
    def pay(self):

        # Card-specific payment message
        print(f"Card payment successful: ₹{self.amount}")


# ---------------------------------------------------
# Creating Objects
# ---------------------------------------------------

# Create a UPI payment object
payment1 = UPIPayment(500)

# Create a Card payment object
payment2 = CardPayment(250)


# ---------------------------------------------------
# Using the Objects
# ---------------------------------------------------

# Process UPI payment
payment1.pay()

# Process Card payment
payment2.pay()


"""
===================================================
DETAILED NOTE: ABSTRACTION
===================================================

What is Abstraction?
--------------------

Abstraction means:

    Hiding unnecessary internal details and exposing
    only the essential operations.

In simple words:

    We know WHAT an object does.

    But we don't need to know HOW it does everything
    internally.


---------------------------------------------------
Understanding Our Example
---------------------------------------------------

We have three classes:

    1. Payment
    2. UPIPayment
    3. CardPayment


Payment:

    It is the parent abstract class.

    It defines a common method:

        pay()

    It tells child classes that they must implement
    this method.


UPIPayment:

    Handles UPI payment.

    It provides its own implementation of:

        pay()


CardPayment:

    Handles Card payment.

    It also provides its own implementation of:

        pay()


---------------------------------------------------
What is ABC?
---------------------------------------------------

First, look at the import:

    from abc import ABC, abstractmethod


ABC stands for:

    Abstract Base Class


We use ABC when we want to create an abstract
parent class.

Look at:

    class Payment(ABC):

This makes Payment an abstract base class.

It is used to define a common structure
for its child classes.


---------------------------------------------------
What is @abstractmethod?
---------------------------------------------------

Look at:

    @abstractmethod
    def pay(self):
        pass


The @abstractmethod decorator marks pay()
as an abstract method.

It tells child classes:

    "You must implement this method."

Here, pass means we are not writing the actual
payment implementation inside the parent class.

The child classes will provide their own
implementations.


---------------------------------------------------
Why Do We Need an Abstract Method?
---------------------------------------------------

Imagine we have different payment methods:

    UPI
    Card
    PayPal


All of them should provide a payment method.

But their internal payment processes can be different.

We don't want every developer to forget to create
a pay() method.

So we define it in the parent abstract class.

    Payment
       |
       | Must implement pay()
       |
       +----------+
       |          |
       ↓          ↓
      UPI        Card
       |          |
       ↓          ↓
     pay()      pay()


Now both child classes must implement pay()
before we can create their objects.


---------------------------------------------------
Why Does pass Exist in Payment?
---------------------------------------------------

Look at:

    def pay(self):
        pass


Here, pass means:

    Do nothing for now.

We are not implementing the payment process
inside the Payment class.

We only define the method that child classes
must provide.


---------------------------------------------------
How Does UPIPayment Implement pay()?
---------------------------------------------------

Look at:

    class UPIPayment(Payment):

UPIPayment inherits from Payment.

Inside the class, we provide:

    def pay(self):
        print(f"UPI payment successful: ₹{self.amount}")


This is called implementing the abstract method.

UPIPayment now has its own pay() method.

It handles payment using its own implementation.


---------------------------------------------------
How Does CardPayment Implement pay()?
---------------------------------------------------

Similarly:

    class CardPayment(Payment):

CardPayment also inherits from Payment.

It provides its own implementation:

    def pay(self):
        print(f"Card payment successful: ₹{self.amount}")


Now both child classes have implemented pay().

Therefore, we can create their objects.


---------------------------------------------------
Can We Create a Payment Object Directly?
---------------------------------------------------

Try this:

    payment = Payment()


Python will raise a TypeError.

Why?

Because Payment contains an abstract method:

    pay()


The method has not been implemented in Payment.

An abstract class with unimplemented abstract methods
cannot be instantiated (used to create an object).

We create objects from child classes that implement
the required abstract methods.


---------------------------------------------------
What Happens If a Child Class Does Not Implement
the Abstract Method?
---------------------------------------------------

Imagine:

    class UPIPayment(Payment):

        def __init__(self, amount):
            self.amount = amount


Here, UPIPayment inherits from Payment but does
not implement pay().

Now try:

    payment1 = UPIPayment(500)


Python will raise a TypeError.

Why?

Because UPIPayment has not implemented the
required abstract method:

    pay()


This is how Python makes sure child classes
follow the structure defined by the parent class.


---------------------------------------------------
Why Is Abstraction Useful?
---------------------------------------------------

Imagine building a real payment application.

We may support:

    UPI
    Credit Card
    Debit Card
    PayPal
    Net Banking


Each payment method has its own implementation.

But all payment methods should provide:

    pay()


By using an abstract class, we can define
a common structure for all payment methods.

This makes our code:

    - More organized.
    - Easier to maintain.
    - Easier to extend.
    - More consistent.


---------------------------------------------------
Simple Definition
---------------------------------------------------

Abstraction means:

    Hiding unnecessary implementation details
    and exposing only the essential operations.


In Python, we can use:

    ABC

    @abstractmethod


---------------------------------------------------
Main Idea
---------------------------------------------------

The parent abstract class defines:

    WHAT child classes must provide.


The child classes define:

    HOW they implement it.


In our example:

    Payment defines pay().

    UPIPayment implements pay() for UPI.

    CardPayment implements pay() for Card.


That is the main idea of Abstraction.
"""
