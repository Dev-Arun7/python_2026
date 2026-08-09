
class Car:
    shop_name = "Auto Focus"
    car_count = 0
    car_id = 0
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        self.running = False
        Car.car_count += 1
        Car.car_id += 1
        self.id = Car.car_id
        

    def drive(self):
        self.running = True
        print(f"You are driving {self.model}")

    def check_selling(self):
        if self.for_sale:
            print(f"{self.model} is selling")
        else:
            print(f"{self.model} is not available")

    def check_new(self):
        if self.year > 2020:
            print(f"{self.model} is relatively new: ({self.year})")
        else:
            print(f"{self.model} is an old car: {self.year}")

    def check_color(self):
        print(f"{self.model} is a {self.color} car")



    def info(self):
        print(f"car count:{self.id} / {self.car_count}")
        print(f"{self.shop_name}")
        print(f"car model: {self.model}")
        print(f"year:   {self.year}")
        print(f"color: {self.color}")
        print(f"for sale: {'Yes' if self.for_sale else 'No'}")

