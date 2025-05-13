class BankAccount: 
    def __init__(self, owner, balance=0):
        self.owner = owner             # Public
        self.balance = balance        # Projected (by convention)
        self.__account_number = "123"       # Private (name mangled)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False
    
    def withdraw(self, amount):
        if 0 < amount<= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self):
        return self.balance
    

account = BankAccount("John", 1000)
print(account.owner)               # John
print(account.balance)              # 1000 (accessible but shouldn't be accessed)
# print(account.__account_number)            # AttributeError
print(account._BankAccount__account_number)   # 123 (accessible through name mangling)
