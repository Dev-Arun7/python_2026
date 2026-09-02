

class Vehicle:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f" The car is {self.value}"
    
    def start(self):
        print("Start car..")

    def stop(self):
        print("Stop car")



# testing
car1 = Vehicle("Tata")
print(car1)
# testing
