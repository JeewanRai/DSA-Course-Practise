class Circle:
    def __init__(self, radius):
        self.radius = radius

    def Area_Circle(self):
        return 3.14 * self.radius * self.radius
    
    def Circumference_Circle(self):
        return 3.14 * 2 * self.radius
    
user_input = float(input("Put radius of the circle: "))

callingclass = Circle(user_input)
callingAreaFun = callingclass.Area_Circle()
callingCircumferenceFun = callingclass.Circumference_Circle()

print('The area of the circle is ', callingAreaFun)
print('The circumference of the circle is ', callingCircumferenceFun)

