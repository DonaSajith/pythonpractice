class BankAccount:
    def interest(self):
        print("General interest")

class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings account interest is 5%")

class CurrentAccount(BankAccount):
    def interest(self):
        print("Current account has no interest")

# # Polymorphism in action
# accounts = [SavingsAccount(), CurrentAccount()]
#
# for acc in accounts:
#     acc.interest()

s= SavingsAccount()
c=CurrentAccount()

s.interest()
c.interest()