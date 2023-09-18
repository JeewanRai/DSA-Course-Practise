""" its creating parent class, a formate to store bank details of individual otherwise we have to write code from scratch, so definig class
will help to make code like hospital priscriptions which is a formate.
while defining BankAccount class its creating formate to store information about bank account of some individuals like, balance,
bank account number otherwise have to write code for depositing in complex way"""

class BankAccount: 
    """ using init method to give features to oject or real perseno that we are trying to create, like talk, walk etc. its called
    creating instance of the class"""
    def __init__(self, account_number, account_holder, balance):
        """self.account_number is attribute uses dot notation espcially used for storing data when object is being created
        the account_number is the variable or value passed on to when the object is created.
        when object is created it calls class i.e. class BankAccount(object), inside of class then the value is passed to each 
        parameters defined in init method, which eventually passed on to assignment paramenter on the right and storing attribute on
        left which is self.account_number or it can be written as self.x = account_numbers as self.x is just to store data when object
        is being created, x is defined init of class so no need to define"""
        self.account_number = account_number #assigning variable to to argument
        self.account_holder = account_holder
        self.balance = balance 

    """creating method to deposit the money in a particular account, this method belogs to class so we use self
    but amount belongs to deposit function we do not use self."""
    def deposit(self, amount):
        if amount > 0: # checking if the amount we are depositing is not -ve, in bank -ve value cannot be deposited
            self.balance += amount # if the if condition is fulfilled it will add the amount in the balance.
            return f"The deposite amout is successful with Nu. {amount:.2f}. Your new balance is {self.balance:.2f}"
        else:
            return f"Invalide deposite"
        
    def withdraw(self, amount): # function to withdraw money form the account
        """will check if amount is more than zero otherwise withdrawing -ve value make no sense 
        also we are checking if the amount we are trying to withdraw i less or equal to available balance that we have in
        our account, if its there we can withdraw the amount"""
        if amount > 0 and amount <= self.balance: 
            self.balance -= amount
            return f"The withdrawn amount is Nu. {amount:.2f}. Your new balance is Nu.{self.balance:.2f}"
        else:
            return f"Insufficient Balance"

    def get_balance(self): # function defined to check balance when ever we required.
        return f"The balance of the {self.account_holder} is Nu. {self.balance:2f}"
    
    def __str__(self):
        return f"Account Number: {self.account_number}\n Account Holder: {self.account_holder}\nAccount Balance: {self.balance:.2f}"
        
"""its creating chield class, which will inherate the features of parent class"""
class SavingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        # inherating features from parent class with command super
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate # self is address of chield class so we use self.interest_rate
    
    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate/100)
        self.balance += interest_amount
        return f"Interest of Nu.{self.interest_rate:.2f} added to your account. Your new balance is Nu.{self.balance:.2f}"
    
    """Object cannot be directly stored, transmitted, or printed wihout converting it to string formate becasue object is a complex
    structure that the machine cannot interprate but converting to stiring formate it becomes easy for machine to intrepret """
    def __str__(self): 
        """In this method super() class is calling the str function of parent class and concatenated with the str function of 
        saving account"""
        return super().__str__() + f"\nInterest Rate: {self.interest_rate}%"

class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        # inherating features from parent class with command super
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit 

    def withdraw(self, amount): # function to withdraw money form the account
        """will check if amount is more than zero otherwise withdrawing -ve value make no sense 
        also we are checking if the amount we are trying to withdraw i less or equal to available balance that we have in
        our account, if its there we can withdraw the amount"""
        if amount > 0 and amount <= self.balance + self.overdraft_limit: 
            self.balance -= amount
            return f"The withdrawn amount is Nu. {amount:.2f}. Your new balance is Nu.{self.balance:.2f}"
        else:
            return f"Insufficient funds including overdraft. Current balance is  {self.balance:.2f}"
        
    def __str__(self):
        return super().__str__() + f"\nOverdraft Limit: Nu.{self.overdraft_limit:.2f}"
    
class Bank:
    def __init__(self):
        # when instance of the bank class created, it initilize empty dictionary called accounts which is called instance variable
        # instance variable is container that holds data for specific object
        # When you call the create_account method of the Bank class, it creates instances of BankAccount, SavingAccount, or CheckingAccount classes, depending on the account
        #  type, and stores these instances as values in the self.accounts dictionary. Each key in the dictionary is the account_number of the 
        # account, and the corresponding value is the account object itself. For example, if you create a savings account with account
        #  number "12345" for Alice, the data for that account is stored in the self.accounts dictionary like this: 
        # {"12345": <SavingsAccount object for Alice>}

        self.accounts = {} #creating account storing dictionary will store data from get account and creat account
    
    def create_account(self, account_number, account_holder, account_type, initial_balance = 0.0, **kwargs):
        if account_number not in self.accounts: # checking account_number in accounts dict., if yes checkes type of account
            if account_type == "Savings":
                account = SavingAccount(account_number, account_holder, initial_balance, **kwargs)
            elif account_type == "Checking":
                account = CheckingAccount(account_number, account_holder, initial_balance, **kwargs)
            else:
                return "Invalid account type"
            
            self.accounts[account_number] = account
            return f"Account created for {account_holder} with {account_number} of account type {account_type}"
        else:
            return "Account number already exist"
        
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found"
            
    def __str__(self):
        account_list = "\n\n".join([str(account) for account in self.accounts.values()])
        return f"Bank Accounts: \n\n{account_list}"
        
bank = Bank()

# creating bank account
print(bank.create_account("12345", "Alice", "Savings", initial_balance=1000.0, interest_rate=2.0))
print(bank.create_account("67890", "Bob", "Checking", initial_balance=500.0, overdraft_limit=100.0))

# Access Bank Accounts
alice_account = bank.get_account("12345")
bob_account = bank.get_account("67890")

# Perform transactions
print(alice_account.deposit(500.0))
print(bob_account.withdraw(700.0))
print(alice_account.add_interest())

print(bank)





        

