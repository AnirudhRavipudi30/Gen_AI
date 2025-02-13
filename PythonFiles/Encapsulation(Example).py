class BankAccount:
    def __init__(self, account_holder, account_type, balance, pin):
        self.account_holder = account_holder  # Public attribute
        self.account_type = account_type  # Public attribute
        self._transaction_history = []  # Protected attribute
        self.__balance = balance  # Private attribute
        self.__pin = pin  # Private attribute
    
    # Method to check balance (Encapsulation: Using a method instead of direct access)
    def get_balance(self, entered_pin):
        if entered_pin == self.__pin:
            return f"Available balance: ${self.__balance}"
        else:
            return "Incorrect PIN! Access denied."

    # Method to deposit money (Encapsulation ensures valid transactions)
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self._transaction_history.append(f"Deposited: ${amount}")
            return f"Deposit successful! New balance: ${self.__balance}"
        return "Invalid deposit amount!"

    # Method to withdraw money (Encapsulation prevents overdraft)
    def withdraw(self, amount, entered_pin):
        if entered_pin == self.__pin:
            if 0 < amount <= self.__balance:
                self.__balance -= amount
                self._transaction_history.append(f"Withdrew: ${amount}")
                return f"Withdrawal successful! Remaining balance: ${self.__balance}"
            return "Insufficient balance!"
        return "Incorrect PIN! Access denied."

    # Protected method to show transaction history (accessible in child classes)
    def _show_transaction_history(self):
        return self._transaction_history

# Child Class: SavingsAccount (Inherits from BankAccount)
class SavingsAccount(BankAccount):
    def show_history(self, entered_pin):
        """Allows viewing transaction history if PIN is correct."""
        if entered_pin == self._BankAccount__pin:  # Accessing private attribute using name mangling
            return self._show_transaction_history()
        return "Incorrect PIN! Cannot access transaction history."

# Example Usage
account = SavingsAccount("Alice", "Savings", 1000, 1234)

print(account.account_holder)  # ✅ Public: Accessible
print(account.get_balance(1234))  # ✅ Private attribute accessed via method
print(account.deposit(500))  # ✅ Deposit money
print(account.withdraw(300, 1234))  # ✅ Withdraw money
print(account.get_balance(9999))  # ❌ Incorrect PIN
print(account.show_history(1234))  # ✅ View transaction history with correct PIN