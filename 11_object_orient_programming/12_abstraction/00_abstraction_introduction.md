# Python OOP: Abstraction

## 1. What is Abstraction?

Abstraction is an Object-Oriented Programming (OOP) concept.

It means:

> Hiding unnecessary internal details and showing only what is needed to
> use something.

In simple words, we don't need to understand how something works
internally to use it.

We only need to know how to use it.

## 2. A Real-World Example: Driving a Car

Think about driving a car.

You use:

-   The start button to start the car.
-   The accelerator to increase speed.
-   The brake to slow down.
-   The steering wheel to change direction.

You don't need to understand:

-   How the engine starts internally.
-   How fuel is injected.
-   How the braking system works.
-   How the transmission changes gears.

The car provides simple controls and hides many internal details.

``` text
       DRIVER
          |
          | Uses
          v
   +---------------+
   |  Car Controls |
   +---------------+
     |     |     |
     v     v     v
   Start  Brake  Steering
          |
          v
   Internal car systems
   (Engine, brakes, etc.)
```

You use the controls without needing to know every detail behind them.

That is the basic idea of Abstraction.

## 3. Why Do We Need Abstraction?

Imagine using a payment system in an application.

We may support different payment methods:

-   UPI
-   Credit Card
-   PayPal

Each payment method works differently internally.

For example:

-   UPI may communicate with a payment service.
-   A card payment may communicate with a card payment gateway.
-   PayPal may use its own payment service.

But from the user's point of view, the main action is simply:

**Make a payment.**

We don't want the user to understand all the internal payment steps.

We want to provide a simple way to use each payment method.

Abstraction helps us create this common structure.

## 4. Abstraction in Python

Python provides a module called `abc` to create abstract base classes.

Two important things from this module are:

### ABC

`ABC` stands for Abstract Base Class.

We use it as a parent class when we want to define a common structure
for other classes.

### @abstractmethod

This decorator marks a method as abstract.

It tells child classes that they must provide their own implementation
of that method.

For example:

``` python
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

Here:

-   `Payment` is an abstract base class.
-   `pay()` is an abstract method.
-   The method has no actual payment implementation here.
-   Child classes must implement `pay()` before their objects can be
    created.

## 5. Why Do We Need an Abstract Class?

Imagine we have three payment methods:

``` text
          Payment
         /   |    \
        /    |     \
       v     v      v
      UPI   Card   PayPal
```

All payment methods should provide a `pay()` method.

But each payment method handles the payment differently.

The `Payment` class defines what every payment method must provide.

The child classes decide how the payment actually happens.

For example:

  Class         Method
  ------------- ---------
  UPI           `pay()`
  CardPayment   `pay()`
  PayPal        `pay()`

The method name is the same, but the implementation is different.

## 6. Can We Create an Object from an Abstract Class?

Normally, we cannot create an object directly from an abstract class if
it still has abstract methods.

For example:

``` python
payment = Payment()
```

This will raise a `TypeError`.

Why?

Because `Payment` has an abstract method called `pay()` that has not
been implemented.

An abstract class is mainly used to define a common structure for its
child classes.

## 7. Abstraction vs Inheritance

These concepts are related, but they have different purposes.

**Inheritance:**

A child class gets features from a parent class.

Example:

``` python
class Dog(Animal):
    pass
```

**Abstraction:**

A parent abstract class defines methods that child classes must
implement.

Example:

``` python
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass
```

A class can use both concepts together.

In fact, we use inheritance when creating child classes from an abstract
base class.

## 8. When Should We Use Abstraction?

Abstraction is useful when:

-   Different classes should follow a common structure.
-   We want child classes to provide certain methods.
-   We want to separate what an object should do from how it does it.
-   We want to work with different implementations through a common
    interface.

For example, a payment system can use different payment methods without
needing to know all their internal details.

## 9. Main Takeaway

Abstraction means:

> Showing what an object can do while hiding unnecessary details about
> how it does it.

In Python, we can use:

-   `ABC` to create an abstract base class.
-   `@abstractmethod` to define methods that child classes must
    implement.

Remember the payment example:

-   Every payment method should have `pay()`.
-   UPI handles payment in its own way.
-   Card payment handles payment in its own way.
-   PayPal handles payment in its own way.

The common structure is defined by the parent class, while the actual
implementation is provided by the child classes.

**In the next example, we will create a `Payment` abstract class and
implement it using `UPIPayment` and `CardPayment`.**
