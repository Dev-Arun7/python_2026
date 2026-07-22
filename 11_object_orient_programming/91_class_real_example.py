import random

class Vehicle:
    def __init__(self, driver):
        self.driver = driver
        self.engine = False
        self.speed = 0
        self.temperature = 0
        self.max_speed = random.randint(75, 150)

    def start_engine(self):
        if not self.engine:
            self.engine = True
        else:
            print("Engine is already running...")

    def accelerate_engine(self):
        if self.engine:
            self.speed += random.randint(1, self.driver.max_acceleration)
            self.temperature += random.randint(10, 30)
            if self.speed > self.max_speed:
                self.speed = self.max_speed
                print("Max speed reached")
        else:
            print("Engine is off...! Please start the engine first")

    def break_car(self):
        self.speed -= random.randint(3, 10)
        if self.speed < 0:
            self.speed = 0

    def park_car(self):
        if not self.engine:
            print("Car already off...")
            return
        self.speed = 0
        self.engine = False
        self.temperature = 0
        print("Car parked...")

class Car(Vehicle):
    def __init__(self, car_name, driver):
        super().__init__(driver)
        self.car_name = car_name

    def __str__(self):
        return f"{self.car_name} | {self.driver.name}"

    def modify_max_speed(self):
        self.max_speed += 5




class Driver:
    def __init__(self, driver_name):
        self.name = driver_name
        self.max_acceleration = random.randint(5, 20)
        self.weight = random.randint(70, 110)

    def __str__(self):
        return f"{self.name}"
    
    def workout(self):
        self.max_acceleration += 1
        self.weight -= 2
        print(f"Driver acceleration increased....: {self.max_acceleration}")

    def eat_junk(self):
        self.weight += 3
        self.max_acceleration -= 1



def race(car1, car2):
    if car1.speed > car2.speed:
        return car1.car_name
    if car2.speed > car1.speed:
        return car2.car_name
    return "DRAW......"



def main():
    driver1 = Driver("Arun")
    driver2 = Driver("Anila")
    car1 = Car("BMW", driver1)
    car2 = Car("Audi", driver2)

    driver1.workout()
    driver1.workout()
    driver1.eat_junk()

    driver2.eat_junk()

    car2.modify_max_speed()
    car1.start_engine()
    car2.accelerate_engine()
    car2.start_engine()
    car2.accelerate_engine()
    car2.accelerate_engine()
    car1.accelerate_engine()
    car1.accelerate_engine()
    car1.break_car()
    car2.break_car()

    result = race(car1, car2)
    car1.park_car()
    car2.park_car()

    print(f"Winner is:   {result}")


    





if __name__ == "__main__":
    main()
    


