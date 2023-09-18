class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0
    
    def read_odometer(self):
        print(f"The updated reading of the odometer is {self.odometer} ")

    def car_description(self):
        print(f"Car is {self.model} of the year {self.year}; make is {self.make}")
        print(f"Method1: Modefying attributes {self.odometer} dircetly")

    def method2_through_method(self, run_year):
        self.odometer = run_year

    def method3_incremental_method(self, run_years):
        self.odometer += run_years

used_car = Car("Suzuki", "CelerioX", 2023)

print(used_car.car_description())

used_car.odometer = 23 #updating odometer reading directly
used_car.read_odometer()

used_car.method2_through_method(53)
used_car.read_odometer()

used_car.method3_incremental_method(100)
used_car.read_odometer()


        
