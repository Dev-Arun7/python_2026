

class Vehicle:
    def start(self):
        print("Start car..")

    def stop(self):
        print("Stop car")

class Car(Vehicle):
    def ac_on(self):
        print("Ac on...")

    def ac_off(self):
        print("AC off..")

class sports_car(Car):
    def reving(self):
        print("Engine revinge....")


car1 = sports_car()
car1.start()
car1.stop()
car1.ac_on()
car1.reving()