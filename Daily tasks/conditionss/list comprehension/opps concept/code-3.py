#task - Create a BankAccount class
# account_holder is public
# balance is private
# Add methods to deposit, withdraw, and check balance
# Do not allow direct acces to balance

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public variable
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrew: {amount}. New Balance: {self.__balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        print(f"Current Balance: {self.__balance}")
# Create an object of BankAccount
account = BankAccount("John Doe", 1000)
# Perform some operations   
account.check_balance()
account.deposit(500)    
account.withdraw(200)
account.check_balance()     
account.withdraw(1500)  # Attempt to withdraw more than balance
account.deposit(-100)  # Attempt to deposit a negative amount
account.withdraw(-50)  # Attempt to withdraw a negative amount
