class Car:
    def __init__(self, make, modle, year ):
        self.make = make
        self.model = modle
        self.year = year
        self.odometer = 0

    def car_description(self):
        print(f"The car is {self.model}, {self.make} of the year {self.year}")
        
    def read_odometer(self):
        print(f"Car odometer reading is {self.odometer}")


my_new_car = Car("Suzuki", "CelerioX", 2023) #creating object of the class, or creating instance of the class
print(my_new_car.car_description())
my_new_car.read_odometer()
