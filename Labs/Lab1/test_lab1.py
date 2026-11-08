import lab1
import unittest

class TestCases(unittest.TestCase):
    def test_same_ends_case_1(self):
        self.assertTrue(lab1.same_ends("test"))

    def test_same_ends_case_2(self):
        self.assertFalse(lab1.same_ends("Incorrect"))

    def test_same_ends_case_3(self):
        self.assertTrue(lab1.same_ends("I"))

    def test_palindromic_case_1(self):
        self.assertTrue(lab1.is_palindromic("racecar"))

    def test_palindromic_case_2(self):
        self.assertFalse(lab1.is_palindromic("salami malaise"))

    def test_palindromic_case_3(self):
        self.assertTrue(lab1.is_palindromic("I"))

    def test_consecutive_sum_case_1(self):
        self.assertEqual(lab1.consecutive_sum(3, 5), 7)

    def test_consecutive_sum_case_2(self):
        self.assertEqual(lab1.consecutive_sum(1, 10), 45)


    # partition: age < 3
    def test_movie_infant_age_0(self):
        self.assertEqual(lab1.get_ticket_price(0), 0)


    # partition: age 3–12
    def test_child_age_3(self):
        self.assertEqual(lab1.get_ticket_price(3), 10)


    def test_child_age_10(self):
        self.assertEqual(lab1.get_ticket_price(10), 10)


    # partition: age 13–64
    def test_teen_age_13(self):
        self.assertEqual(lab1.get_ticket_price(13), 15)


    def test_adult_age_50(self):
        self.assertEqual(lab1.get_ticket_price(50), 15)


    def test_senior_age_90(self):
        self.assertEqual(lab1.get_ticket_price(90), 12)


if __name__ == "__main__":
    unittest.main()
