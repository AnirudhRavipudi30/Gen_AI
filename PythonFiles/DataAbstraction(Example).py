from abc import ABC, abstractmethod  # Importing Abstract Base Class module

# Abstract Parent Class
class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount  # Public attribute

    @abstractmethod
    def process_payment(self):
        """Abstract method: Must be implemented by child classes"""
        pass

# Child Class 1: Credit Card Payment
class CreditCardPayment(Payment):
    def process_payment(self):
        return f"Processing credit card payment of ${self.amount}"

# Child Class 2: PayPal Payment
class PayPalPayment(Payment):
    def process_payment(self):
        return f"Processing PayPal payment of ${self.amount}"

# Child Class 3: Cryptocurrency Payment
class CryptoPayment(Payment):
    def process_payment(self):
        return f"Processing cryptocurrency payment of ${self.amount}"

# Example Usage
payments = [CreditCardPayment(100), PayPalPayment(200), CryptoPayment(300)]

for payment in payments:
    print(payment.process_payment())  # Calls respective child class implementation