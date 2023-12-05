class MinimumBalanceError(Exception):
    pass

class Account:
    AccNumber = 1001
    def __init__(self, name, balance):
        if balance < 1000:
            raise MinimumBalanceError('Account cannot be created, low balance')
        self.name = name
        self.balance = balance
        self.account_number = Account.AccNumber
        Account.AccNumber += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount < 1000:
            raise MinimumBalanceError('Amount cannot be withdrawn')
        self.balance -= amount

    def show_details(self):
        print('Account Number is', self.account_number)
        print('Name', self.name)
        print('Balance', self.balance)

acc1 = Account('John', 2000)
acc1.show_details()

acc2 = Account('Mary', 3000)
acc2.show_details()


acc1.deposit(1000)
acc1.show_details()

acc1.withdraw(2000)
acc1.show_details()
