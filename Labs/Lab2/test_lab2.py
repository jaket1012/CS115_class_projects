# === CS 115 Lab 2 ===
# Fill in your name and the Stevens Honor Code pledge on the following lines.
# Failure to fill this in will result in deducted marks.
#
# Name:Jake Talvy
#
# Pledge:I pledge my honor that I have abided by the Stevens Honor System.
#
# === CS 115 Lab 2 ===

import lab2
import unittest
# You can access vali_date as lab2.vali_date in this file.

class TestCases(unittest.TestCase):
    def test_vali_date_case_1(self):
        """
        Tests that the date May 15th registers as valid.
        """
        self.assertTrue(lab2.vali_date(5, 15))

    def test_vali_date_case_2(self):
        pass # Your test cases here.
        self.assertTrue(lab2.vali_date(1,5))
        self.assertTrue(lab2.vali_date(12,5))
        self.assertFalse(lab2.vali_date(0,5))
        self.assertFalse(lab2.vali_date(13,5))
        self.assertTrue(lab2.vali_date(5,31))
        self.assertFalse(lab2.vali_date(5,32))
        self.assertTrue(lab2.vali_date(5,1))
        self.assertFalse(lab2.vali_date(5,0))
        self.assertFalse(lab2.vali_date(4,31))
        self.assertTrue(lab2.vali_date(4,30))
        self.assertFalse(lab2.vali_date(2,30))
        self.assertTrue(lab2.vali_date(2,29))
if __name__ == "__main__":
    unittest.main()
