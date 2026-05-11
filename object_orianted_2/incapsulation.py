class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        
    def deposit(self, amount):
        if amount <=  0:
            return f"Deposition amount must be positive"
        
        self._balance = self._balance + amount
        
    def account_info(self):
        return f"Account holder {self._name} has {self._balance} tk balance"
    

account1 = BankAccount("John Doe", 1000)

print(account1.account_info())
account1.deposit(500)
print(account1.account_info())