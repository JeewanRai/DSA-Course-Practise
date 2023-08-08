
def even_odd():
    
    while 1:
        user_input = int(input('Enter the number: '))

        if user_input%2 == 0:
            if user_input%4 ==0:
                print("Multiple of 4")
            else: 
                 print("The number is even")
        else:
            print("The number is odd")

        choice = input("Wanna try for another number? (YES/NO)!: ")

        check = int(input("User check number: "))
        if user_input % check == 0:
            print(f'{check} evenly divideds {user_input}')
        else:
             print(f'{check} not evenly divideds {user_input}')
      
        if choice.upper() != "YES":   
            break
even_odd()
