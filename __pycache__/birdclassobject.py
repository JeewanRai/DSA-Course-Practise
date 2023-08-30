class Bird: #creating parent class or creating bule print for the object called Bird
    def __init__(self, name, age, color): #initilizing the attributes or properties of the brid class to create object
       self.name = name
       self.age = age
       self.color = color 

    def action(self):
        print(f'I am {name}, I can fly')
    
class Hen(Bird): #creating chield class from the Bird class or parent class which is inheretence
    def __init__(self):
        super().__init__(name, age, color)
        print(f'I am one of kid of bird named {name}')

    def action(self): # overridding method used for parent class
        print(f'I am {name}, I cant fly')
    
    def run(self):
        print('I can run fast')

hen = Hen()



                