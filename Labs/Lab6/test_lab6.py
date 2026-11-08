import lab6
import unittest

class TestCases(unittest.TestCase):
    def test_to_int_case_1(self):
        tup = (5, 3, 7, 9,)
        self.assertEqual(lab6.to_int(tup, 10), 5379)

    def test_to_int_case_2(self):
        tup = (1, 2, 1,)
        self.assertEqual(lab6.to_int(tup, 10), 121)
        self.assertEqual(lab6.to_int(tup, 3), 16)

    def test_to_int_case_3(self):
        tup = (1,0,0,1,0,1,1,0,1)
        self.assertEqual(lab6.to_int(tup, 2), 301)

    def test_to_int_case_4(self):
        tup = (15, 14,)
        self.assertEqual(lab6.to_int(tup, 16), 254)

    def test_to_base_case_1(self):
        tup = (5, 3, 7, 9,)
        self.assertEqual(lab6.to_base(5379, 10), tup)

    def test_to_base_case_2(self):
        tup = (1, 2, 1,)
        tup2 = (1, 1, 1, 1, 1)
        self.assertEqual(lab6.to_base(121, 10), tup)
        self.assertEqual(lab6.to_base(121, 3), tup2)

    def test_to_base_case_3(self):
        tup = (1,0,0,1,0,1,1,0,1)
        self.assertEqual(lab6.to_base(301, 2), tup)

    def test_to_base_case_4(self):
        tup = (15, 14,)
        self.assertEqual(lab6.to_base(254, 16), tup)

if __name__ == "__main__":
    unittest.main()
