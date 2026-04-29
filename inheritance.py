class BankAccount:
    def deposit(self):
        print("Money deposited")

class SavingsAccount(BankAccount):
    def interest(self):
        print("Interest added")

s = SavingsAccount()
s.deposit()
s.interest()