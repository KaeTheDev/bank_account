class BankAccount:
    accounts = []  # Class variable to store instances

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)  # Add instance to the list

    def deposit(self, amount):
        self.balance += amount
        print(f"You deposited {amount} into your account! Your new balance is {self.balance}")
        return self
        
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"You withdrew {amount}. Your new balance is {self.balance}")
        else:
            print("Insufficient Funds: Charging a $5 fee.")
            self.balance -= 5.0
            print(f"Your new balance is {self.balance}")
        return self
            
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        if self.balance >= 0:
            interest = self.balance * self.int_rate
            self.balance += interest
            print(f"Your new balance with interest is {self.balance}")
        else:
            print("Your balance is too low to add interest.")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts:
            print("Account Information:")
            print("Interest Rate:", account.int_rate)
            print("Balance:", account.balance)
            print("\n==============\n")

# TEST USER ONE
print("JANES ACCOUNT")
janesAccount = BankAccount(0.03, 100)

janesAccount.deposit(100.00).deposit(2000.00).deposit(200.00).withdraw(3000.00).yield_interest().display_account_info()

print("\n==============\n")

#TEST USER TWO
print("JOHNS ACCOUNT")
johnsAccount = BankAccount(0.03, 1000)

johnsAccount.deposit(500).deposit(100).deposit(200).withdraw(100).withdraw(200).withdraw(300).withdraw(600).display_account_info()

print("\n==============\n")

# Using the class method to print all account information
BankAccount.print_all_accounts()
