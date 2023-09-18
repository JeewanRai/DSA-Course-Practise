class Car: #creating blue print or prototype to build the car object
    def __init__(self, make, model, year): # d\efining parameters and attributes that the car object must hold
        self.make = make #assigning varaible make into attribute self.make where self determies the address of the objet
        self.model = model
        self.year = year
        self.odometer = 0

    def car_description(self):
        return f"The make of the car is {self.make}; model is {self.model} of the year {self.year}"
    
    def read_odometer(self):
        return f"The odometer reading of the care is {self.read_odometer}"
    
    def update_odometer(self, milage):
        if milage >= self.read_odometer:
            self.odometer = milage 
        else:
            print("You cant roll back to odometer")

    def incremental_method_updateodometer(self, update):
        self.read_odometer += update

class ElectricCar(Car):
    def __init__(self, make, model, year): #good practise to again defnied make, model and year of the parent class in the chield class
    #chield class cannot access the attributes and method of parent class directly, if changes made to chield class it will 
    #affect the logic of the parent class therefore we use super() to call the attributes and method of parent class
        super().__init__(make, model, year) 
        self.battery_life = 7
    
    def battery_life_then(self):
        return f"The battery life of the care is {self.battery_life}"

my_car = ElectricCar('MG', 'MG ZS', 2023)
print(my_car.car_description())
print(my_car.battery_life_then())

    
