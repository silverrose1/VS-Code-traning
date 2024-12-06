class Account:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance
    self.transactions = []

  def deposit(self, amount=0): #deposit function
    if 0 < amount :
      self.balance += amount
      self.transactions.append(f"Deposit: {amount}")
    return self.balance
      
  def withdraw(self, amount=0): #withdraw function
    if 0 < amount <= self.balance:
      self.balance -= amount
      self.transactions.append(f"Withdrawal: {amount}")
    return self.balance
