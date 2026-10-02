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
        if self._balance - amount:
            print("Enter a valid amount, insufficient funds!")
        else:
            print(f"Withdrew {amount}. New balance: {self._balance}")


class CheckingAccount(Account):
    def __init__(self, owner_name, balance, overdraft_limit):
        super().__init__(owner_name, balance)
        self.overdraft_limit = overdraft_limit

    def get_withdrawal_fee(self):
        return 5

    def withdraw(self, amount):
        fee = self.get_withdrawal_fee()
        total_deduction = amount + fee
        if self._balance - total_deduction < -self.overdraft_limit:
            print("Enter a valid amount, insufficient funds!")
        else:
            self._balance -= total_deduction
            print(f"Withdrew {amount} (+{fee} fee). New balance: {self._balance}")


class PremiumAccount(CheckingAccount):
    def __init__(self, owner_name, balance, over_draft_limit):
        super().__init__(owner_name, balance, over_draft_limit)
        self.overdraft_limit = over_draft_limit

    def get_withdrawal_fee(self):
            return 0

    def withdraw(self, amount):
        fee = self.get_withdrawal_fee()
        total_deduction = amount + fee
        if self._balance - total_deduction < -self.overdraft_limit:
            print("Enter a valid amount, insufficient funds!")
        else:
            self._balance -= total_deduction
            print(f"Withdrew {amount} (+{fee} fee). New balance: {self._balance}")



checking = CheckingAccount("Rohan", 100, 500)
checking.withdraw(50)

premium = PremiumAccount("Asha", 100, 500)
premium.withdraw(50)





