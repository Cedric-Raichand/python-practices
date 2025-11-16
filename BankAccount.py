class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
            return
        self.balance -= amount
        print(f"Withdrawn: {amount}")

    def get_balance(self):
        print(f"Balance for {self.owner}: {self.balance}")


# TESTING THE SYSTEM
acc = BankAccount("Cedric", 200)
acc.deposit(100)
acc.withdraw(50)
acc.get_balance()