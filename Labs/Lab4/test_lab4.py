import lab4
import unittest

class TestCases(unittest.TestCase):
    def test_factorial_case_1(self):
        self.assertEqual(lab4.factorial(3), 6)

    def test_factorial_case_2(self):
        self.assertEqual(lab4.factorial(1), 1)

    def test_factorial_case_3(self):
        self.assertEqual(lab4.factorial(5), 120)

    def test_factorial_case_4(self):
        self.assertEqual(lab4.factorial(0), 1)

    def test_power_seq_case_1(self):
        out = (1, 3, 9, 27,)
        self.assertAlmostEqual(lab4.power_seq(3, 3), out)

    def test_power_seq_case_2(self):
        out = (1,)
        self.assertAlmostEqual(lab4.power_seq(5, 0), out)

    def test_power_seq_case_3(self):
        out = (1, 1.5, 2.25,)
        self.assertAlmostEqual(lab4.power_seq(1.5, 2), out)

    def test_power_seq_case_4(self):
        out = (1, -1, 1, -1,)
        self.assertAlmostEqual(lab4.power_seq(-1, 3), out)

    def test_len_case_1(self):
        inp = (1, 2, 3, 4,)
        self.assertEqual(lab4.my_len(inp), 4)

    def test_len_case_2(self):
        inp = ("Hello", "it's", "me",)
        self.assertEqual(lab4.my_len(inp), 3)

    def test_len_case_3(self):
        inp = ()
        self.assertEqual(lab4.my_len(inp), 0)

    def test_len_case_4(self):
        inp = (("Nested", "tuples"), ("don't", "contribute"),)
        self.assertEqual(lab4.my_len(inp), 2)

    def test_dot_case_1(self):
        xs = (1, 1, 1,)
        ys = (2, 3, 4,)
        self.assertAlmostEqual(lab4.dot(xs, ys), 9.0)

    def test_dot_case_2(self):
        xs = (1.0, 0.5, 0.25, 0.125,)
        ys = (10.0, 20.0, 40.0, 80.0,)
        self.assertAlmostEqual(lab4.dot(xs, ys), 40.0)

    def test_dot_case_3(self):
        xs = ()
        ys = ()
        self.assertAlmostEqual(lab4.dot(xs, ys), 0.0)

    def test_dot_case_4(self):
        xs = (5, 2, 8, 3)
        ys = (3.14, 2.71, 1.44, 1.61)
        self.assertAlmostEqual(lab4.dot(xs, ys), 37.47)

    def test_poly_case_1(self):
        coeffs = (1, 1, 0.5,)
        self.assertAlmostEqual(lab4.poly(coeffs, 2), 5.0)

    def test_poly_case_2(self):
        coeffs = (1.0, 0.0, -1.0)
        self.assertAlmostEqual(lab4.poly(coeffs, 1.0), 0.0)

    def test_poly_case_3(self):
        coeffs = (0, 0, 0, 0, 0, 0, 0,)
        self.assertAlmostEqual(lab4.poly(coeffs, 100.0), 0.0)

    def test_poly_case_4(self):
        coeffs = (1, 4, 6, 4, 1)
        self.assertAlmostEqual(lab4.poly(coeffs, 3), 256)

if __name__ == "__main__":
    unittest.main()
