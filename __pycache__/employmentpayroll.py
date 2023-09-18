# creating employment class with attributes were all the emloyee will have name, id and salary
class Employee:
    # special method called constructor which is defined/special instruction given to create object 
    # with certain attributes or behaviour an object should have which will get called automatically
    # when new object is created
    def __init__(self, name, emp_id, salary):
        self.name = name 
        self.emp_id = emp_id
        self.salary = salary

class TaxtCalculator:
    @staticmethod
    def calculate_taxt(salary):
         #if salary <= 50000:
            #return salary * 0.1
        #else:
            #return salary * 0.2
        
        taxt_rate = 0.1 if salary <= 50000 else 0.2
        tax = salary * taxt_rate






employee1 = Employee("Jeewan", 293, 50000)
print(employee1.name)
print(employee1.emp_id)
print(employee1.salary)