"""Creating programm to store data in empty list through user input.
User will input number of time program to be iterated and using forloop program will iterate with user input value inside of the for loop.
The user input value will be appended to empty list"""

list_empty = []

user_input = int(input("Enter the user number for iteration: "))

for number in range(0, user_input):
    input_iterable_value = int(input("Number for iteration: "))
    list_empty.append(input_iterable_value)
    
print(list_empty)
