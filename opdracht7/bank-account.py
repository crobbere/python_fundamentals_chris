class BankAccount():
    
    def __init__(self, owner, balance=0.0):
        self.owner= owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        self.balance -=amount
        return self.balance

account = BankAccount("Alex")
print(account.owner)
print(account.balance)
print(account.deposit(10))
print(account.withdraw(3))
