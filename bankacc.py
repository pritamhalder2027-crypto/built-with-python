from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(Account):
    def withdraw(self, amount):
        if amount > self._balance:
            print("Enter a valid amount, insufficient funds!")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance: {self._balance}")

class CheckingAccount(Account):
    def __init__(self, owner_name, balance, overdraft_limit):
        super().__init__(owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.overdraft_limit:
            print(f"Withdrew {amount}. New balance: {self._balance}")
        else:
            print("Enter a valid amount, insufficient funds!")

checking = CheckingAccount("Rohan", 100, 500)
checking.withdraw(300)
checking.withdraw(700)

