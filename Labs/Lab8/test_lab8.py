import unittest
import lab8

a1 = [[[1]]]  # 1x1x1
a2 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]  # 2x2x2
a4 = [[[1, 2], [3, 4]]]  # 1x2x2
a5 = [
    [[ 1,  2], [ 3,  4]],
    [[ 5,  6], [ 7,  8]],
    [[ 9, 10], [11, 12]]
] # non-cubic


class TestCopy3D(unittest.TestCase):

    def test_same_values_1x1x1(self):
        b = lab8.copy_3d(a1)
        self.assertEqual(a1, b)

    def test_different_outer_object(self):
        b = lab8.copy_3d(a2)
        self.assertIsNot(a2, b)

    def test_inner_lists_are_distinct(self):
        b = lab8.copy_3d(a2)
        self.assertIsNot(a2[0], b[0])
        self.assertIsNot(a2[0][0], b[0][0])

    def test_modifying_copy_does_not_affect_original(self):
        b = lab8.copy_3d(a2)
        b[0][0][0] = 999
        self.assertNotEqual(a2[0][0][0], b[0][0][0])

    def test_non_cubic_shape(self):
        b = lab8.copy_3d(a4)
        self.assertEqual(a4, b)
        self.assertIsNot(a4, b)
        self.assertIsNot(a4[0], b[0])


class TestCheckCopy3D(unittest.TestCase):

    def test_true_deep_copy_returns_true(self):
        l1 = [[[1, 2], [3, 4]]]
        l2 = [[[1, 2], [3, 4]]]
        self.assertTrue(lab8.check_copy_3d(l1, l2))

    def test_reference_copy_returns_false(self):
        l1 = [[[1, 2], [3, 4]]]
        l2 = l1  
        self.assertFalse(lab8.check_copy_3d(l1, l2))

    def test_modified_one_value_copy_returns_false(self):
        l1 = [[[1, 2], [3, 4]]]
        l2 = [[[1, 2], [3, 4]]]
        l2[0][0][0] = 999 
        self.assertFalse(lab8.check_copy_3d(l1, l2))

    def test_structure_mismatch_returns_false(self):
        l1 = [[[1, 2], [3, 4]]]
        l2 = [[[1, 2]]]  # missing a sublist
        self.assertFalse(lab8.check_copy_3d(l1, l2))

    def test_on_own_copy3d(self):
        l1 = a5
        l2 = lab8.copy_3d(a5)
        self.assertTrue(lab8.check_copy_3d(l1, l2))



if __name__ == "__main__":
    unittest.main()

