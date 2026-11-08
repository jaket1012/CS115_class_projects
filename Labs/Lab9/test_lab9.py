import lab9
import unittest

class TestCases(unittest.TestCase):
    def test_init_case_1(self):
        bob = lab9.Employee("Bob", 10)
        self.assertEqual("Bob", bob.name)
        self.assertIs(None, bob.manager)

    def test_init_case_2(self):
        bob = lab9.Employee("Bob", 10)
        self.assertEqual("Bob", bob.name)
        self.assertEqual(10, bob.id)

    def test_init_case_3(self):
        bob = lab9.Employee("Bob", 10)
        sally = lab9.Employee("Sally", 9)
        bob2 = lab9.Employee("Bob", 10)
        self.assertIsNot(bob2, bob)

    def test_init_case_4(self):
        bob = lab9.Employee("Bob", 10)
        sally = lab9.Employee("Sally", 9)
        bob2 = lab9.Employee("Bob", 8)
        self.assertNotEqual(sally.id, bob.id)
        self.assertNotEqual(bob2.id, bob.id)

    def test_assign_case_1(self):
        bob = lab9.Employee("Bob", 10)
        manny = lab9.Employee("Manny", 9)
        manny.assign(bob)
        self.assertIs(manny, bob.manager)
        self.assertIs(None, manny.manager)

    def test_assign_case_2(self):
        alex  = lab9.Employee("Alex", 1)
        bob = lab9.Employee("Bob", 2)
        manny = lab9.Employee("Manny", 3)
        alex.assign(manny)
        manny.assign(bob)
        self.assertIs(manny, bob.manager)
        self.assertIs(alex, manny.manager)
        self.assertIs(None, alex.manager)

    def test_assign_case_3(self):
        alex  = lab9.Employee("Alex", 1)
        bob = lab9.Employee("Bob", 2)
        manny = lab9.Employee("Manny", 3)
        alex.assign(bob)
        self.assertIs(alex, bob.manager)
        manny.assign(bob)
        self.assertIs(manny, bob.manager)

    def test_assign_case_4(self):
        alex  = lab9.Employee("Alex", 1)
        bob = lab9.Employee("Bob", 2)
        alex.assign(bob)
        bob.assign(alex)
        self.assertIs(alex, bob.manager)
        self.assertIs(bob, alex.manager)

    def test_eq_case_1(self):
        alex  = lab9.Employee("Alex", 1)
        bob = lab9.Employee("Bob", 2)
        self.assertNotEqual(alex, bob)

    def test_eq_case_2(self):
        alex  = lab9.Employee("Alex", 5)
        bob = lab9.Employee("Bob", 5)
        self.assertNotEqual(alex, bob)

    def test_eq_case_3(self):
        alex = lab9.Employee("Bob", 1)
        bob = lab9.Employee("Bob", 2)
        self.assertNotEqual(alex, bob)

    def test_eq_case_4(self):
        alex = lab9.Employee("Bob", 5)
        bob = lab9.Employee("Bob", 5)
        self.assertEqual(alex, bob)
        bob.manager = alex
        self.assertEqual(alex, bob)

    def test_str_case_1(self):
        bob = lab9.Employee("Bob", 5)
        self.assertEqual("5: Bob", str(bob))

    def test_str_case_2(self):
        alex = lab9.Employee("Alex", 7000)
        self.assertEqual("7000: Alex", str(alex))

    def test_str_case_3(self):
        bob = lab9.Employee("Bob", 5)
        alex = lab9.Employee("Alex", 4)
        bob.manager = alex
        self.assertEqual("5: Bob (Managed by 4: Alex)", str(bob))

    def test_str_case_4(self):
        bob = lab9.Employee("Bob", 5)
        alex = lab9.Employee("Alex", 4)
        self.assertEqual("5: Bob", str(bob))
        bob.manager = alex
        self.assertEqual("5: Bob (Managed by 4: Alex)", str(bob))

    def test_promote_case_1(self):
        bob = lab9.Employee("Bob", 1)
        manny = lab9.Employee("Alex", 2)
        alex = lab9.Employee("Alex", 3)
        bob.manager = manny
        manny.manager = alex
        self.assertIs(manny, bob.manager)
        bob.promote()
        self.assertIs(alex, bob.manager)
        self.assertIs(alex, manny.manager)

    def test_promote_case_2(self):
        bob = lab9.Employee("Bob", 1)
        alex = lab9.Employee("Alex", 2)
        bob.manager = alex
        self.assertIs(alex, bob.manager)
        bob.promote()
        self.assertIs(None, bob.manager)
        self.assertIs(None, alex.manager)

    def test_promote_case_3(self):
        bob = lab9.Employee("Bob", 1)
        self.assertIs(None, bob.manager)
        bob.promote()
        self.assertIs(None, bob.manager)

    def test_promote_case_4(self):
        bob = lab9.Employee("Bob", 1)
        manny = lab9.Employee("Alex", 2)
        alex = lab9.Employee("Alex", 3)
        sam = lab9.Employee("Sam", 4)
        sam.manager = alex
        bob.manager = manny
        manny.manager = alex
        self.assertIs(manny, bob.manager)
        bob.promote()
        self.assertIs(alex, bob.manager)
        bob.promote()
        self.assertIs(None, bob.manager)
        self.assertIs(alex, sam.manager)

    def test_org_depth_case_1(self):
        bob = lab9.Employee("Bob", 1)
        self.assertEqual(1, bob.org_depth())

    def test_org_depth_case_2(self):
        bob = lab9.Employee("Bob", 100)
        alex = lab9.Employee("Alex", 200)
        bob.manager = alex
        self.assertEqual(1, alex.org_depth())
        self.assertEqual(2, bob.org_depth())

    def test_org_depth_case_3(self):
        bob = lab9.Employee("Bob", 200)
        manny = lab9.Employee("Alex", 300)
        alex = lab9.Employee("Alex", 400)
        sam = lab9.Employee("Sam", 500)
        sam.manager = alex
        bob.manager = manny
        manny.manager = alex
        self.assertEqual(3, bob.org_depth())
        bob.promote()
        self.assertEqual(2, bob.org_depth())
        bob.promote()
        self.assertEqual(1, bob.org_depth())

    def test_org_depth_case_4(self):
        bob1 = lab9.Employee("Bob", 1)
        bob2 = lab9.Employee("Bob", 2)
        bob3 = lab9.Employee("Bob", 3)
        bob4 = lab9.Employee("Bob", 4)
        bob5 = lab9.Employee("Bob", 5)
        bob6 = lab9.Employee("Bob", 6)
        bob6.manager = bob5
        bob5.manager = bob3
        bob4.manager = bob3
        bob3.manager = bob1
        bob2.manager = bob1
        self.assertEqual(1, bob1.org_depth())
        self.assertEqual(2, bob2.org_depth())
        self.assertEqual(2, bob3.org_depth())
        self.assertEqual(3, bob4.org_depth())
        self.assertEqual(3, bob5.org_depth())
        self.assertEqual(4, bob6.org_depth())

if __name__ == "__main__":
    unittest.main()
