from car import Car  # importing class


# creating object
car1 = Car("mustang", 2022, "red", False)
car2 = Car("Tata", 2019, "black", True)
car3 = Car("Suzuki", 2025, "white", False)
car4 = Car("Tayota", 2015, "blue", True)
car5 = Car("BYD", 2021, "black", True)



cars = [car1, car2, car3, car4, car5]


for car in cars:
    print("-" * 30)
    car.info()

    car.drive()
    car.check_color()
    car.check_selling()
    car.check_new()