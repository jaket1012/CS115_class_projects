import lab0
import unittest

class TestCases(unittest.TestCase):
    def test_find_zero_case_1(self):
        self.assertEqual(-1.0, lab0.find_zero(1, 1))

    def test_find_zero_case_2(self):
        self.assertEqual(10.0, lab0.find_zero(0.5, -5))

    def test_find_zero_case_3(self):
        self.assertEqual(0.5, lab0.find_zero(-4, 2))

    def test_find_zero_case_4(self):
        self.assertIsNone(lab0.find_zero(0, 5))

if __name__ == "__main__":
    unittest.main()
