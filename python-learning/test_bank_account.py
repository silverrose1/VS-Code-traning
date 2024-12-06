import unittest
from a import Account

class TestAccount(unittest.TestCase):

    def test_initial_balance(self):
        account = Account(100)
        self.assertEqual(account.balance, 100)

    def test_default_initial_balance(self):
        account = Account()
        self.assertEqual(account.balance, 0)

    def test_deposit_positive_amount(self):
        account = Account(50)
        account.deposit(50)
        self.assertEqual(account.balance, 100)

    def test_deposit_zero_amount(self):
        account = Account(50)
        account.deposit(0)
        self.assertEqual(account.balance, 50)

    def test_deposit_negative_amount(self):
        account = Account(50)
        account.deposit(-20)
        self.assertEqual(account.balance, 50)

    def test_withdraw_positive_amount(self):
        account = Account(100)
        account.withdraw(50)
        self.assertEqual(account.balance, 50)

    def test_withdraw_zero_amount(self):
        account = Account(100)
        account.withdraw(0)
        self.assertEqual(account.balance, 100)

    def test_withdraw_exceeding_balance(self):
        account = Account(50)
        account.withdraw(100)
        self.assertEqual(account.balance, 50)

    def test_withdraw_negative_amount(self):
        account = Account(50)
        account.withdraw(-20)
        self.assertEqual(account.balance, 50)

    def test_withdraw_float(self):
        account = Account(100.0)
        account.withdraw(50.5)
        self.assertEqual(account.balance, 49.5)

    def test_transaction_history_deposit(self):
        account = Account(50)
        account.deposit(30)
        self.assertEqual(account.transactions, ["Deposit: 30"])

    def test_transaction_history_withdraw(self):
        account = Account(100)
        account.withdraw(25)
        self.assertEqual(account.transactions, ["Withdrawal: 25"])
        
    def test_transaction_history_multiple(self):
        account = Account(100)
        account.deposit(50)
        account.withdraw(20)
        account.deposit(10)

        self.assertEqual(account.transactions, ["Deposit: 50", "Withdrawal: 20", "Deposit: 10"])



if __name__ == '__main__':
    unittest.main()
