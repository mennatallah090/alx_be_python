class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        print(f"Deposited: ${amount:.1f}")

    def withdraw(self, amount):
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        else:
            self.account_balance -= amount
            print(
                f"Withdrew: ${amount:.1f}. New balance: ${self.account_balance:.1f}")  # Display amount and balance with one decimal place
            return True

    def display_balance(self):
        # print(f"Your current balance is: ${self.account_balance}")
        print(f"Current Balance: ${self.account_balance:.2f}")  # Corrected line
