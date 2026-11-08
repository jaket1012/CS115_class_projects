import lab3
import unittest


class TestCases(unittest.TestCase):
    def test_mean_case_1(self):
        data = (1, 2, 3, 4, 5)
        self.assertAlmostEqual(lab3.mean(data), 3)

    def test_mean_case_2(self):
        data = (1, 4, 5, 10, 7)
        self.assertAlmostEqual(lab3.mean(data), 5.4)

    def test_rms_case_1_no_invalid(self):
        data = (1, 3, 3, 5, 6)
        self.assertAlmostEqual(lab3.rms(data), 4)

    def test_rms_case_2_contains_invalid(self):
        data = (0, 4, None, 8, 8, None)
        self.assertAlmostEqual(lab3.rms(data), 6)

    def test_rms_case_3_negative(self):
        data = (-7, -1, 1, 4, 7, 10)
        self.assertAlmostEqual(lab3.rms(data), 6)

    def test_hm_case_1(self):
        data = (1, 3)
        self.assertAlmostEqual(lab3.hm(data), 1.5)

    def test_hm_case_2_has_invalid(self):
        data = (1, 3, 3, None)
        self.assertAlmostEqual(lab3.hm(data), 1.8)


if __name__ == "__main__":
    unittest.main()
