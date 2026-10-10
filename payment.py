class Payment:
    def __init__(self, amount):
        self.amount = amount

    def pay(self):
        print("Processing payment of: ", self.amount)

class UPIPayment(Payment):
     def pay(self):
         print("Processing UPI Payment of: ", self.amount, "With no fee")

class CreditCardPayment(Payment):
    def pay(self):
        print("Credit Card Payment of: ", self.amount, ":+ 2% fee")

p1 = CreditCardPayment(2000)
p1.pay()

p2 = UPIPayment(500)
p2.pay()

