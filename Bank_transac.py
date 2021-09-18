class Account:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account Owner : {self.owner}  \n Balance is : {self.balance}'
        # print('\n Account balance : '.format(self.balance))

    def deposit(self, amount):

        self.balance += amount
        print('Deposit is sucessfull & current balance in the account is : {}'.format(self.balance))

    def withdraw(self, amount):

        if amount < self.balance:
            self.balance = self.balance - amount
            print('Withdrawal is sucessfull & remaining balance in the acount is {}'.format(self.balance))
        else:
            print('There is no sufficient balance in the account')


myAc = Account('Kalai', 100)

print(myAc)

myAc.deposit(100)

myAc.withdraw(50)