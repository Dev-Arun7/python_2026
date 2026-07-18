import random


# ==========================================================
# Car Class
# ----------------------------------------------------------
# Represents a single car.
#
# The Car object stores:
# - Car information (name, fuel, speed)
# - Current driver
#
# The Car knows how to:
# - Start
# - Stop
# - Accelerate
# - Brake
# - Show its status
# ==========================================================
class Car:

    def __init__(self, car_name, driver):
        # Basic information
        self.car_name = car_name
        self.fuel = 20
        self.speed = 0
        self.engine = False

        # Store the Driver object.
        # We keep the whole object instead of copying
        # values like driver.name or driver.acceleration.
        self.driver = driver

    # Called automatically when print(car) is used.
    def __str__(self):
        return f"{self.car_name} | speed={self.speed}"

    # Turn on the engine.
    def start(self):
        self.engine = True
        print(f"{self.driver.name} started {self.car_name}")

    # Turn off the engine.
    def stop(self):
        self.engine = False
        print(f"{self.driver.name} stopped {self.car_name}")

    # Increase the speed.
    #
    # The driver's acceleration skill affects
    # how much the speed increases.
    def accelerate(self):
        print("Accelerating....")
        self.speed += random.randint(1, self.driver.acceleration)
        print("Speed:", self.speed)

    # Reduce the speed.
    def breake_car(self):
        print("Breaking.....")
        self.speed -= random.randint(1, 10)
        print(f"Speed is: {self.speed}")

    # Print all information about this car.
    def status(self):
        print(f"---------{self.car_name}----------")
        print(f"Engine : {self.engine}")
        print(f"Speed  : {self.speed}")
        print(f"Fuel   : {self.fuel}")
        print(f"Driver : {self.driver.name}")
        print("--------------------------")


# ==========================================================
# Driver Class
# ----------------------------------------------------------
# Represents one driver.
#
# Every driver has different abilities.
# Later we can add:
# - experience
# - age
# - reaction_time
# - driving_skill
# ==========================================================
class Driver:

    def __init__(self, name):
        self.name = name
        self.top_speed = random.randint(100, 200)
        self.acceleration = random.randint(5, 20)
        self.height = random.randint(150, 190)


# ==========================================================
# Helper Functions
# ----------------------------------------------------------
# These are not part of the Car class.
# They coordinate objects.
# ==========================================================

# Perform a driving routine.
def drive(car):
    car.start()
    car.accelerate()
    car.accelerate()
    car.breake_car()
    car.accelerate()
    car.status()


# Perform a parking routine.
def park(car):
    car.breake_car()
    car.stop()
    car.status()


# Compare two cars and return the winner.
def race(car1, car2):

    if car1.speed > car2.speed:
        return car1.car_name

    elif car2.speed > car1.speed:
        return car2.car_name

    return "Draw"


# ==========================================================
# Main Function
# ----------------------------------------------------------
# Create all objects.
# Connect them together.
# Run the program.
# ==========================================================
def main():

    driver1 = Driver("Arun")
    driver2 = Driver("Akhil")

    car1 = Car("BMW", driver1)
    car2 = Car("AUDI", driver2)

    drive(car1)
    drive(car2)

    winner = race(car1, car2)

    print(f"\nWinner: {winner}")


# Program starts here.
if __name__ == "__main__":
    main()