

class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating.")

    def sleep(self):
        print(f"{self.name} is sleeping.")



class Dog(Animal):
    def speak(self):
        print(f"{self.name} is barking")
        print("BOW  WOOF  WOOF   WOOF")

class Cat(Animal):
    

class Mouse(Animal):
    pass


# Creating objects
dog = Dog("Killer") # Yes, that dog in Tom & Jerry
cat = Cat("Tom")  # Why not Tom.....
mouse = Mouse("Jerry") # Obviously.


# Using dog object
print(dog.name)