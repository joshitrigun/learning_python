class AccountBalanceException(Exception):
    pass


balance = 10000


def withdraw(amount):
    global balance

    if balance - amount < 5000:
        raise AccountBalanceException('Balance should not be less than 5000')
    else:
        balance = balance - amount
        print('Remaining balance is', balance)


try:
    withdraw(6000)
except AccountBalanceException as e:
    print(e)
