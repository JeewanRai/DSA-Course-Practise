class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposit of Nu.{amount:.2f} is successful. Your new balance is {self.balance:.2f}"
        else:
            return f"Invalid deposit"

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn of Nu.{amount:.2f} is successful. Your new balance is {self.balance:.2f}"
        else:
            return f"Insufficient balance"

    def get_balance(self):
        return f"The balance of {self.account_holder} is Nu.{self.balance:.2f}"

    def __str__(self):
        return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder}\nAccount Balance: Nu.{self.balance:.2f}"


class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, interest_rate):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.balance += interest_amount
        return f"Interest of Nu.{interest_amount:.2f} added. Your new balance is {self.balance:.2f}"

    def __str__(self):
        return super().__str__() + f"\nInterest Rate: {self.interest_rate}%"


class CheckingAccount(BankAccount):
    def __init__(self, account_number, account_holder, balance, overdraft_limit):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            return f"Withdrawn of Nu.{amount:.2f} is successful. Your new balance is {self.balance:.2f}"
        else:
            return f"Insufficient funds (including overdraft). Current balance is {self.balance:.2f}"

    def __str__(self):
        return super().__str__() + f"\nOverdraft Limit: Nu.{self.overdraft_limit:.2f}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, account_type, initial_balance=0.0, **kwargs):
        if account_number not in self.accounts:
            if account_type == "Savings":
                account = SavingsAccount(account_number, account_holder, initial_balance, **kwargs)
            elif account_type == "Checking":
                account = CheckingAccount(account_number, account_holder, initial_balance, **kwargs)
            else:
                return "Invalid account type"
            
            self.accounts[account_number] = account
            return f"Account created for {account_holder} with account number {account_number} of type {account_type}"
        else:
            return "Account number already exists."

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found"

    def __str__(self):
        account_list = "\n\n".join([str(account) for account in self.accounts.values()])
        return f"Bank Accounts:\n\n{account_list}"


# Usage
bank = Bank()

# Create Bank Accounts
print(bank.create_account("12345", "Alice", "Savings", initial_balance=1000.0, interest_rate=2.0))
print(bank.create_account("67890", "Bob", "Checking", initial_balance=500.0, overdraft_limit=100.0))

# Access Bank Accounts
alice_account = bank.get_account("12345")
bob_account = bank.get_account("67890")

# Perform transactions
print(alice_account.deposit(500.0))
print(bob_account.withdraw(700.0))
print(alice_account.add_interest())

# Display account details
print(bank)
