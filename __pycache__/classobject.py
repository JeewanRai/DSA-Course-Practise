class Animal: # creating drawing or blue print of the Animal
    def __init__(self, name, legs, color): # initilizing the parameters of animal class, using paramaterized method, with parameters
        self.name = name
        self.legs = legs
        self.color = color

    def sound(self): # defining another function for sound of the animal
        print("I am", self.name)

class Human(Animal): # inhereting attributes of Animal class to Human class
    def __init__(self, name): 
        super().__init__(name)
        print("Human created: ", self.name)

    def sound(self): # overriding and the concept of Polymorphism, where sound function is over written
        print("I am Human, my name is: ", self.name) 

class Dog(Animal): # inhereting attributes of Animal class to Human class
    def __init__(self, name): 
        super().__init__(name)
        print("Human created: ", self.name)

    def sound(self): # overriding and the concept of Polymorphism, where sound function is over written
        print("I am Dog, my name is: ", self.name)    #https://github.com/ddayto21/HackerRank-Python-Solutions/blob/main/Classes-Tutorial.ipynb