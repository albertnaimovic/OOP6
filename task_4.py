# Create a simple bank account class, BankAccount, with the following specifications:

# The BankAccount class should have an attribute balance which starts at 0.
# It should have an instance method deposit that allows an amount to be added to the balance.
# It should have an instance method withdraw that allows an amount to be taken from the balance. If the balance is less than the withdrawal amount,
# print a message that says "Insufficient funds".
# Add a class method from_balance that takes a starting balance as an argument and returns a new BankAccount instance with that starting balance.
# Add a static method transfer that takes two BankAccount instances and an amount as arguments.
# It should withdraw the amount from the first account and deposit it into the second account.


class BankAccount:
    def __init__(self, balance: float = 0.0) -> None:
        self.balance = balance

    def deposit(self, amount: float) -> float:
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds")

    @classmethod
    def from_balance(cls, starting_balance: float) -> "BankAccount":
        balance = starting_balance
        return cls(balance)

    @staticmethod
    def transfer(account_1: "BankAccount", account_2: "BankAccount", amount):
        account_1.withdraw(amount)
        account_2.deposit(amount)


account_1 = BankAccount.from_balance(5000.0)
account_2 = BankAccount()

print(account_1.balance)
account_1.withdraw(1000.0)
print(account_1.balance)
account_1.deposit(250.0)
print(account_1.balance)
BankAccount.transfer(account_1=account_1, account_2=account_2, amount=15.5)
print(account_1.balance)
print(account_2.balance)
