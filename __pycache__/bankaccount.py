class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.acount_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount>0:
            self.balance += amount
            return f"Deposit of Nu.{amount:.2f} is successful. Your new balance is {self.balance:.2f}" #2f is used for rounding up
        else:
            return f"Invalid deposit"
    def withdrawd(self, amount):
        if amount > 0 and amount <= self.balance: # if amount to withdraw is more than balance, it cant be drawn
            self.balance -= amount 
            return f"Withdrawn of Nu.{amount:.2f} is successful. Your new balance is {self.balance:.2f}" #2f is used for rounding up
        else:
            return f"Insufficient balance"
        
    def get_balance(self):
        return f"The balance of the {self.account_holder} is Nu.{self.balance:.2f}"

    def __str__(self):
        return "Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nAccount Balance: Nu.{self.balance:2f}"
    
class Bank: 
    def __init__(self): 
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance = 0.0):
        if account_number not in self.accounts:
            account = BankAccount(account_number, account_holder, initial_balance)
            return f"Account created for {account_holder} with {account_holder}"
        else:
            return "Account number already exist."
    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else: 
            return "Account not found"
        
    def __str__(self):
        account_list = "\n\n".join([str(account) for account in self.accounts.values()])
        return f"Bank Accounts:\n\n{account_list}"
    
bank = Bank()

# Create Bank Accounts
print(bank.create_account("12345", "Alice", 1000.0))
print(bank.create_account("67890", "Bob", 500.0))

# Access Bank Accounts
alice_account = bank.get_account("12345")
bob_account = bank.get_account("67890")











