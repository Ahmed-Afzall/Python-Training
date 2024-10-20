'''
Question: Define a class Account with private attributes for account_number and balance. 
Implement methods to deposit and withdraw money, ensuring that the balance cannot be directly 
accessed or modified from outside the class. Demonstrate the use of these methods.
'''
# class declaration
class Account:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # private attribute
        self.__balance = balance  # private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance is ${self.__balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance is ${self.__balance}.")
        else:
            print("Insufficient balance or invalid amount.")

    def get_balance(self):
        return self.__balance

# Demonstrating the use of deposit and withdraw methods
account = Account("123456789", 1000)
account.deposit(500)
account.withdraw(200)
print("Balance:", account.get_balance())

edited