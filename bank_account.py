# Python program to create a BankAccount class and add objects and methods

class BankAccount:
  def __init__ (self, owner, balance):
    self.owner = owner
    self.balance = balance

  def deposit(self, deposit):
    self.balance = self.balance + deposit
    print(f"Deposited ${deposit} to {self.owner}'s account")

  def withdraw(self, withdraw):
    if withdraw > self.balance:
      print(f"Insufficient funds! Cannot withdraw ${withdraw} from {self.owner}'s account")
      return
    self.balance = self.balance - withdraw
    print(f"Withdrew ${withdraw} from {self.owner}'s account")

  def check_balance(self):
    print(f"Current Balance is : ${self.balance}")

  def display_account_info(self):
    print(f"{self.owner}'s account balance : ${self.balance}")

name = input("Enter your name : ")
initial_deposit = float(input("Enter initial deposit amount : "))
account = BankAccount(name, initial_deposit)

while True:
  action = input("Would you like to deposit, withdraw, or exit? ").strip().lower()

  if action == "exit":
    print("Exiting account session.")
    break

  if action not in ["deposit", "withdraw"]:
    print("Invalid choice. Please type deposit, withdraw, or exit.")
    continue

  amount_text = input(f"Enter amount to {action} : ").strip()
  try:
    amount = float(amount_text)
  except ValueError:
    print("Invalid amount. Please enter a numeric value.")
    continue

  if amount <= 0:
    print("Amount must be greater than 0.")
    continue

  if action == "deposit":
    account.deposit(amount)
  else:
    account.withdraw(amount)

  account.check_balance()

account.display_account_info()
