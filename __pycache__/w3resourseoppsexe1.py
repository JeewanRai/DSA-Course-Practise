class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area(self):
        return  3.14 * self.radius

    def Parameters(self):
        return 2 * 3.14 * self.radius

radius = float(input("Enter the value of the radius: ")) # taking user input

circle = Circle(radius) # creating object of the Circle class
area = circle.Area()
parameter = circle.Parameters()

print(f'The area of the Circle is {area}')
print(f'The parameter of the Circle is {parameter}')
