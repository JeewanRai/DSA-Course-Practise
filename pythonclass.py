class student:
    '''Dock string'''
    #company = 'Hruk Holding & Investment' #static value
    # this line of function when called will display same value as its fixed
    # in order to use different argument when called we define argument inside function
    #def __init__(self):
        #self.name = 'Jeewan'
        #self.roll = 1010
        #self.mark = 73.3
    def __init__(self, name, roll, mark):
        self.name = name
        self.roll = roll
        self.mark = mark
        student.company = 'Druk Holding & Investment' # another method to creat static variable

    def __str__(self):
        return 'This is first python class'
    
    def display(self):
        print('Student name', self.name)
        print('Roll Number', self.roll)
        print('Marks', self.mark)
        print('The name of the company is ', student.company)
    
#calling_function = student()
#calling_function.display()


# anotehr method to call static variable before calling object of the call
#student.company = "Druk Holding & Investment"
#calfun = student('Jeewan', 1010, 94)
#calfun1 = student('Sonam', 1012, 49)
#calfun2 = student('Dorji', 1912, 82)


calfun = [student('Jeewan', 1010, 94), student('Sonam', 1012, 49), student('Dorji', 1912, 82)]

for i in calfun:
    i.display()

#calfun.display()
#calfun1.display()
#calfun2.display()

#print(calling_function.name)
#print(calling_function.mark)
#print(calling_function.roll)