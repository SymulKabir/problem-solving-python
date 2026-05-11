class PaymentMethod:
    def __init__(self,amount):
        self.amount = amount
    def make_payment(self):
        pass
        

class CreditCard(PaymentMethod):
    def make_payment(self):
        return f"Processing credit card payment of {self.amount}"
    
class DebitCard(PaymentMethod):
    def make_payment(self):
        return f"Processing debit card payment of {self.amount}"






c_payment = CreditCard(140)
d_payment = DebitCard(100)
print(c_payment.make_payment())
print(d_payment.make_payment())
    