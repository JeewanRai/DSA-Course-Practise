class CurrentAccount:
    def __init__(self, name):
        self.name = name # self.name is instance variable that store data of each instance of class
        self.balance = 0
        
    # self.name and self.balance can be accessed by both the methods
    def get_customer_name(self):
        return self.name
    
    def get_customer_balance(self): # instance method associated with CurrentAccount class or object of current account
        return self.balance
    
account_holder = CurrentAccount("Jeewan Rai")
print("The name of the customer is:", account_holder.get_customer_name())
print("The balance of the customer is:", account_holder.get_customer_balance())