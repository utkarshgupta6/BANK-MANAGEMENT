import unittest
from database import accounts
from banking_operations import check_balance, withdraw_money, deposit_money, authenticate_user

class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        accounts["100A"] = [1234, 150000.0, "Utkarsh"]
        accounts["100B"] = [5678, 25000.0, "Harsh"]

    def test_authenticate_success(self):
        status, name = authenticate_user("100A", 1234)
        self.assertTrue(status)

    def test_check_balance(self):
        balance = check_balance("100A")
        self.assertEqual(balance, 150000.0)

    def test_deposit_success(self):
        status, new_balance = deposit_money("100A", 5000.0)
        self.assertTrue(status)
        self.assertEqual(new_balance, 155000.0)

    def test_withdraw_success(self):
        status, new_balance = withdraw_money("100A", 10000.0)
        self.assertTrue(status)
        self.assertEqual(new_balance, 140000.0)

if __name__ == "__main__":
    unittest.main()
