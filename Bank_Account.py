# Python program to create a BankAccount class and add objects and methods

class BankAccount:
  def __init__ (self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, deposit):
    self.balance = self.balance + deposit
    print(f"Deposited ${deposit} to {self.owner}'s account")

  def withdraw(self, withdraw):
    self.balance = self.balance - withdraw
    print(f"Withdrew ${withdraw} from {self.owner}'s account")

  def check_balance(self):
    print(f"Current Balance is : ${self.balance}")

  def display_account_info(self):
    print(f"{self.owner}'s account balance : ${self.balance}"

account = BankAccount("John",1000)
account.deposit(500)
account.withdraw(200)
account.check_balance()
account.display_account_info()
