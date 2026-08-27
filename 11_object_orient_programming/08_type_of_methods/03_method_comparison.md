# Python OOP: Instance Method vs Class Method vs Static Method

## Introduction

In Python, methods are functions that are written inside a class.

There are **3 common types of methods**:

1. **Instance Method**
2. **Class Method**
3. **Static Method**

The main difference is **what the method needs to work with**.

A simple way to remember:

```text
Instance method → works with an object
Class method    → works with the class
Static method   → does not need the object or class
```

---

# 1. Instance Method

An **instance method** works with the data of a particular object.

It is the most common type of method in Python classes.

## Example

```python
class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def get_info(self):
        print(f"{self.name} {self.gpa}")


student1 = Student("Arun", 6.1)
student2 = Student("Anila", 8.6)

student1.get_info()
student2.get_info()
```

Output:

```text
Arun 6.1
Anila 8.6
```

Here:

```python
student1.get_info()
```

`get_info()` works with the data of `student1`.

And:

```python
student2.get_info()
```

works with the data of `student2`.

## Why do we need `self`?

`self` refers to the **current object**.

For example:

```python
student1.get_info()
```

Python internally gives the method the `student1` object.

So we can think of it approximately like:

```python
Student.get_info(student1)
```

Therefore:

```python
self.name
self.gpa
```

means:

```text
name of the current object
gpa of the current object
```

## When should we use an instance method?

Use an instance method when the method needs information from a particular object.

For example:

```text
Student
    ↓
student1 → Arun, 6.1
student2 → Anila, 8.6
```

If the method needs `student1`'s name or GPA, an instance method is appropriate.

---

# 2. Class Method

A **class method** works with data that belongs to the class itself.

We create a class method using:

```python
@classmethod
```

The first parameter is normally:

```python
cls
```

`cls` refers to the **class**.

## Example

```python
class Student:
    student_count = 0

    def __init__(self, name):
        self.name = name
        Student.student_count += 1

    @classmethod
    def get_student_count(cls):
        return cls.student_count


student1 = Student("Arun")
student2 = Student("Anila")
student3 = Student("Akhil")

print(Student.get_student_count())
```

Output:

```text
3
```

Here:

```python
student_count
```

belongs to the **class**, not to one particular student.

So a class method is suitable.

## Why do we need `cls`?

`cls` refers to the class.

In this example:

```python
@classmethod
def get_student_count(cls):
    return cls.student_count
```

`cls` refers to:

```python
Student
```

So:

```python
cls.student_count
```

is basically accessing:

```python
Student.student_count
```

---

# 3. Static Method

A **static method** is a method that does not need:

- the object (`self`)
- the class (`cls`)

We create it using:

```python
@staticmethod
```

## Example

```python
class Student:

    @staticmethod
    def is_pass(gpa):
        return gpa >= 5


print(Student.is_pass(6.1))
print(Student.is_pass(3.5))
```

Output:

```text
True
False
```

Notice that this method does not need:

```python
self
```

or:

```python
cls
```

It simply receives a value and performs an operation.

---

# Why Put a Static Method Inside a Class?

You might ask:

> "If it doesn't use the object or class, why not just create a normal function?"

That is a very good question.

You **can** create a normal function.

For example:

```python
def is_pass(gpa):
    return gpa >= 5
```

But sometimes the function is strongly related to the class.

For example:

```python
class Student:

    @staticmethod
    def is_pass(gpa):
        return gpa >= 5
```

Now the method is grouped logically with `Student`.

We can call:

```python
Student.is_pass(6.1)
```

This tells us:

> "This operation is related to Student."

So static methods are useful for **helper operations related to a class**.

---

# The Main Difference

Here is the most important comparison:

| Method | First parameter | Works with | Decorator |
|---|---|---|---|
| Instance method | `self` | Object | Nothing required |
| Class method | `cls` | Class | `@classmethod` |
| Static method | Nothing | Neither object nor class | `@staticmethod` |

---

# Simple Mental Model

Imagine we have:

```python
class Student:
    ...
```

There are three different levels.

```text
                 Student CLASS
                       |
          ---------------------------
          |                         |
      Class data                Objects
   student_count          -------------------
                          |        |        |
                       student1 student2 student3
```

### Instance method

Works with:

```text
student1
student2
student3
```

Uses:

```python
self
```

### Class method

Works with:

```text
Student class
```

Uses:

```python
cls
```

### Static method

Doesn't need either one.

```text
Student
   |
   └── helper operation
```

---

# One Class Showing All Three

Let's put all three methods together.

```python
class Student:
    student_count = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

        Student.student_count += 1

    # Instance method
    def get_info(self):
        return f"{self.name} - {self.gpa}"

    # Class method
    @classmethod
    def get_student_count(cls):
        return cls.student_count

    # Static method
    @staticmethod
    def is_pass(gpa):
        return gpa >= 5


student1 = Student("Arun", 6.1)
student2 = Student("Anila", 8.6)

# Instance method
print(student1.get_info())

# Class method
print(Student.get_student_count())

# Static method
print(Student.is_pass(6.1))
```

Output:

```text
Arun - 6.1
2
True
```

---

# What Does Each Method Need?

## Instance Method

Needs:

```text
Object
  ↓
self
```

Example:

```python
student1.get_info()
```

Use it when the method needs object-specific data.

---

## Class Method

Needs:

```text
Class
  ↓
cls
```

Example:

```python
Student.get_student_count()
```

Use it when the method needs class-level data.

---

## Static Method

Needs:

```text
Nothing
```

Example:

```python
Student.is_pass(6.1)
```

Use it when the operation is related to the class but does not need object or class data.

---

# Important: Can We Call Them Using Objects?

Yes, Python allows some different ways of calling methods.

For beginners, it is better to use the clearest style.

## Instance method

Normally call using an object:

```python
student1.get_info()
```

Because it works with that object.

## Class method

Normally call using the class:

```python
Student.get_student_count()
```

Because it works with class-level data.

## Static method

Normally call using the class:

```python
Student.is_pass(6.1)
```

Because it doesn't need a particular object.

---

# When Should I Choose Which One?

Ask yourself this question:

## Question 1

> Does this method need data from a particular object?

If **YES**:

```python
def method(self):
```

Use an **instance method**.

Example:

```python
def get_info(self):
    return self.name
```

---

## Question 2

> Does this method need data belonging to the class?

If **YES**:

```python
@classmethod
def method(cls):
```

Use a **class method**.

Example:

```python
@classmethod
def get_student_count(cls):
    return cls.student_count
```

---

## Question 3

> Does this method need neither object data nor class data?

If **YES**:

```python
@staticmethod
def method():
```

Use a **static method**.

Example:

```python
@staticmethod
def is_pass(gpa):
    return gpa >= 5
```

---

# Easy Decision Chart

```text
                 What does the method need?
                           |
             +-------------+-------------+
             |             |             |
         Object?         Class?        Neither?
             |             |             |
             ↓             ↓             ↓
         Instance       Class         Static
          method        method        method
             |             |             |
           self           cls       no self/cls
```

---

# Real-Life Example

Imagine a `BankAccount` class.

```python
class BankAccount:

    bank_name = "ABC Bank"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
```

### Instance method

Checking the account balance:

```python
def get_balance(self):
    return self.balance
```

Why?

Because every account has a different balance.

```text
Arun account  → ₹10,000
Anila account → ₹25,000
```

So we need `self`.

---

### Class method

Changing the bank name:

```python
@classmethod
def change_bank_name(cls, name):
    cls.bank_name = name
```

Why?

Because `bank_name` belongs to the class.

So we use `cls`.

---

### Static method

Checking whether an amount is valid:

```python
@staticmethod
def valid_amount(amount):
    return amount > 0
```

Why?

It doesn't need a particular account or the bank class.

It only needs the `amount`.

---

# Common Beginner Mistake

Do not think:

```text
self = object
cls = object
```

They are different.

Remember:

```text
self → current object
cls  → current class
```

For example:

```python
student1 = Student("Arun", 6.1)
```

When we do:

```python
student1.get_info()
```

`self` refers to:

```text
student1
```

When we do:

```python
Student.get_student_count()
```

`cls` refers to:

```text
Student
```

---

# Another Important Difference

An instance method can access both:

```python
self.name
Student.student_count
```

A class method can access class data:

```python
cls.student_count
```

but it does not have a particular `self` object.

A static method does not automatically receive either:

```python
self
```

or:

```python
cls
```

It only works with the values that you explicitly give it.

---

# Quick Comparison

| Feature | Instance Method | Class Method | Static Method |
|---|---|---|---|
| Decorator | None | `@classmethod` | `@staticmethod` |
| First parameter | `self` | `cls` | None |
| Gets object automatically? | Yes | No | No |
| Gets class automatically? | Yes, indirectly through object/class | Yes | No |
| Can access object data easily? | Yes | No | No |
| Can access class data? | Yes | Yes | No |
| Main purpose | Object-specific work | Class-specific work | Related helper operation |

---

# The Most Important Thing to Remember

Don't choose a method based only on whether it is possible.

Choose it based on **what the method is supposed to work with**.

```text
                    METHOD
                       |
        What does it need to work with?
                       |
        +--------------+--------------+
        |              |              |
      Object          Class        Neither
        |              |              |
        ↓              ↓              ↓
      self            cls         staticmethod
        |              |              |
    Instance          Class         Static
     method           method        method
```

## Final Summary

### Instance Method

```python
def get_info(self):
```

Use when you need information from a **specific object**.

### Class Method

```python
@classmethod
def get_count(cls):
```

Use when you need information or want to change something at the **class level**.

### Static Method

```python
@staticmethod
def check_value(value):
```

Use when you need **neither object data nor class data**, but the operation is logically related to the class.

The easiest memory trick is:

```text
self → object
cls  → class
static → neither
```

Once you understand these three, choosing the correct method becomes much easier.
