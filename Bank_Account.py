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
    print(f"{self.owner}'s account balance : ${self.balance}")

name = input("Enter your name : ")
initial_deposit = float(input("Enter initial deposit amount : "))
account = BankAccount(name, initial_deposit)
deposit_amount = float(input("Enter deposit amount : "))
account.deposit(deposit_amount)
withdraw_amount = float(input("Enter withdrawal amount : "))
account.withdraw(withdraw_amount)
account.check_balance()
account.display_account_info()
