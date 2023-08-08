dict_number = {'UK':100, 'UK':[100, "Python"], 'India':(200, "Hello World")}
print(dict_number)

#adding new element in the dictionalry 
dict_number['Australia'] = [3000, "Jeewan"]
print(dict_number)

#deleting the item from the dictionary
del(dict_number['Australia'])
print(dict_number)

#alternate way to remove using pop function
print(dict_number.pop('UK', None), dict_number)

#length function to determine the length of the key pairs
print(len(dict_number))

#using loop in the dictionary, cannot use range function in the dictrionary since data in the dictionary is indicated by key 
#cannot use membership operator on the value, only can use in the key 
for number in dict_number:
    print(number, dict_number[number])

