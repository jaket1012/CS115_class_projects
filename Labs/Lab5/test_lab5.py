import lab5
import unittest

class TestCases(unittest.TestCase):
    def test_coin_change_case_1(self):
        coins = (50, 26, 1)
        self.assertEqual(lab5.coin_change(coins, 52), 2)

    def test_coin_change_case_2(self):
        coins = (100, 5, 10, 25, 1)
        self.assertEqual(lab5.coin_change(coins, 67), 6)

    def test_coin_change_case_3(self):
        coins = (1, 10, 12, 15)
        self.assertEqual(lab5.coin_change(coins, 52), 4)

    def test_coin_change_case_4(self):
        coins = (1, 10, 11, 25)
        self.assertEqual(lab5.coin_change(coins, 31), 3)

    def test_coin_change_case_5(self):
        coins = (1, 2, 4, 8, 16, 32)
        self.assertEqual(lab5.coin_change(coins, 46), 4)

    def test_coin_change_case_6(self):
        coins = (1, 2, 3, 5, 8, 13, 21, 34)
        self.assertEqual(lab5.coin_change(coins, 51), 4)

if __name__ == "__main__":
    unittest.main()
