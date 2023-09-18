class Employee: #creating blue print of employee class, defining what employee can have and what they can do
    #constructor init special method is called to give some attributes to object, associate specific data to object
    def __init__(self, id, first_name, last_name, salary): #after creating blue print they should assign some properties line id
        self.id = id # self.id is attribute, its place where parameter/variable id is stored so it get bound to class employee
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def annual_salary(self):
        return 12*self.salary
    
    def increament(self, amount):
       self.salary += amount
       return self.salary 
    
employee1 = Employee(239, "Jeewan", "Rai", 2000) #creating object 1
employee2 = Employee(233, "Sonam", "Dorji", 50000) #creating object 2

print(employee1.full_name()) # call full name fundtion
print(employee2.full_name())

amount = float(input("Enter incremenet amount: "))

print(employee1.increament(amount))
print(employee2.increament(amount))




        















