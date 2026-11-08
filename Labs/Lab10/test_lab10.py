import unittest
import lab10

class TestCases(unittest.TestCase):
    def test_task1_give_raise_case_1(self):
        bob = lab10.Employee("Bob", 0)
        self.assertEqual(0, bob.salary)
        bob.give_raise(1000)
        self.assertEqual(1000, bob.salary)

    def test_task1_give_raise_case_2(self):
        bob = lab10.Employee("Bob", 0)
        manny = lab10.Employee("Manny", 1)
        alex = lab10.Employee("Alex", 2)
        manny.assign(bob)
        alex.assign(manny)
        self.assertEqual(0, bob.salary)
        self.assertEqual(0, alex.salary)
        self.assertEqual(0, manny.salary)
        bob.give_raise(1000)
        self.assertEqual(1000, bob.salary)
        self.assertEqual(1000, alex.salary)
        self.assertEqual(1000, manny.salary)

    def test_task1_give_raise_case_3(self):
        gary = lab10.Employee("Gary", 0)
        bob = lab10.Employee("Bob", 1)
        manny = lab10.Employee("Manny", 2)
        alex = lab10.Employee("Alex", 3)
        bob.salary = 1000
        manny.salary = 2000
        alex.salary = 5000
        bob.assign(gary)
        manny.assign(bob)
        alex.assign(manny)
        self.assertEqual(0, gary.salary)
        self.assertEqual(1000, bob.salary)
        self.assertEqual(2000, manny.salary)
        self.assertEqual(5000, alex.salary)
        gary.give_raise(1500)
        self.assertEqual(1500, gary.salary)
        self.assertEqual(1500, bob.salary)
        self.assertEqual(2000, manny.salary)
        self.assertEqual(5000, alex.salary)

    def test_task2_mentor_inherits_employee(self):
        assert issubclass(lab10.Mentor, lab10.Employee)

    def test_task2_mentor_case_1(self):
        bob = lab10.Employee("Bob", 0)
        manfred = lab10.Mentor("Manfred", 1)
        self.assertIs(None, manfred.mentee)
        manfred.assign_mentee(bob)
        self.assertIs(bob, manfred.mentee)
        self.assertTrue(isinstance(manfred, lab10.Employee))

    def test_task2_mentor_case_2(self):
        bob = lab10.Employee("Bob", 1)
        manfred = lab10.Mentor("Manfred", 2)
        self.assertIs(None, manfred.mentee)
        manfred.assign(bob)
        manfred.assign_mentee(bob)
        self.assertIs(None, manfred.mentee)
        bob.manager = None
        manfred.assign_mentee(bob)
        self.assertIs(bob, manfred.mentee)

    def test_task2_mentor_case_3(self):
        jan = lab10.Employee("Jan", 0)
        bob = lab10.Employee("Bob", 1)
        manfred = lab10.Mentor("Manfred", 2)
        manny = lab10.Employee("Manny", 3)
        alex = lab10.Employee("Alex", 4)
        alex.assign(manny)
        alex.assign(manfred)
        manny.assign(bob)
        bob.assign(jan)
        manfred.assign_mentee(jan)
        self.assertIs(bob, jan.manager)
        self.assertEqual(4, jan.org_depth())
        manfred.recommend()
        self.assertIs(manny, jan.manager)
        self.assertEqual(3, jan.org_depth())


    def test_task3_embezzler_case_1(self):
        bob = lab10.Employee("Bob", 1)
        emb = lab10.Embezzler("Emmy Bezzler", 2)
        manny = lab10.Employee("Manny", 3)
        emb.assign(bob)
        manny.assign(emb)
        self.assertIs(manny, emb.manager)
        self.assertEqual(0, emb.salary)
        self.assertEqual("Emmy Bezzler", emb.name)

    def test_task3_embezzler_case_2(self):
        emb = lab10.Embezzler("Emmy Bezzler", 0)
        emb.salary = 5000
        emb.give_raise(10000)
        self.assertEqual(15000, emb.salary)

    def test_task3_embezzler_case_3(self):
        emb = lab10.Embezzler("Emmy Bezzler", 0)
        emb.salary = 20000
        emb.give_raise(10000)
        self.assertEqual(20000, emb.salary)

    def test_task3_embezzler_case_4(self):
        bob = lab10.Employee("Bob", 1)
        emb = lab10.Embezzler("Emmy Bezzler", 2)
        manny = lab10.Employee("Manny", 3)
        emb.assign(bob)
        manny.assign(emb)
        bob.salary = 1000
        emb.salary = 1500
        manny.salary = 4000
        bob.give_raise(3000)
        self.assertEqual(3000, bob.salary)
        self.assertEqual(4500, emb.salary)
        self.assertEqual(4500, manny.salary)

    def test_task4_manager_inherits_employee(self):
        assert issubclass(lab10.Manager, lab10.Employee)

    def test_task4_manager_case_1(self):
        manny = lab10.Manager("Manny", 1)
        self.assertIs(None, manny.manager)
        self.assertEqual(0, manny.salary)
        self.assertEqual("Manny", manny.name)
        self.assertEqual([], manny.reports)

    def test_task4_manager_case_2(self):
        bob = lab10.Employee("Bob", 1)
        manny = lab10.Manager("Manny", 2)
        manny.assign(bob)
        self.assertIs(manny, bob.manager)
        self.assertEqual([bob], manny.reports)

    def test_task4_manager_case_3(self):
        bob = lab10.Employee("Bob", 1)
        manny = lab10.Manager("Manny", 2)
        manfred = lab10.Manager("Manfred", 3)
        manny.assign(bob)
        self.assertIs(manny, bob.manager)
        self.assertEqual([bob], manny.reports)
        self.assertEqual([], manfred.reports)
        manny.reassign(manfred)
        self.assertIs(manfred, bob.manager)
        self.assertEqual([], manny.reports)
        self.assertEqual([bob], manfred.reports)

if __name__ == "__main__":
    unittest.main()
