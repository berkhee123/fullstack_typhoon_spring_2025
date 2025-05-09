class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner # Public attribute
        self._balance = balance # "Private" attribute (by convention)
        self.__account_number = "12345" # Name mangled attribute


account = BankAccount("John")
print(account.owner) # Accessible: John
print(account._balance) # Accessible but shouldn't be acceseed directly: 0
# print(account.__account_number) # AttibuteError
print(account.__BankAccount_account_number) # Accessible throught mangled name: 12345
