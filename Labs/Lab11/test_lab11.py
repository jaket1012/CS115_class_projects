import unittest
import lab11

class TestGridFunctions(unittest.TestCase):

    def test_accumulate_costs_single_row(self):
        row = [1, 4, 9]
        self.assertEqual(lab11.accumulate_costs(row), [1,5,14] )

    def test_accumulate_costs_single_element(self):
        row = [7]
        self.assertEqual(lab11.accumulate_costs(row), [7])

    def test_accumulate_costs_single_row_contains_0(self):
        row = [10,5,2,0,3]
        self.assertEqual(lab11.accumulate_costs(row),[10,15,17,17,20])


    def test_accumulate_col_costs_first_column(self):
        grid = [[4, 1],
                [7, 3],
                [2, 5]]
        self.assertEqual(lab11.accumulate_col_costs(grid, 0), [4, 11, 13])

    def test_accumulate_col_costs_second_column(self):
        grid = [[4, 1], [7, 3], [2, 5]]
        self.assertEqual(lab11.accumulate_col_costs(grid, 1), [1, 4, 9])

    def test_accumulate_col_costs_single_row(self):
        grid = [[9, 8, 7]]
        self.assertEqual(lab11.accumulate_col_costs(grid, 2), [7])

    def test_accumulate_col_costs_negative_values(self):
        grid = [[-2, 3], [-1, -3], [5, 1]]
        self.assertEqual(lab11.accumulate_col_costs(grid, 1), [3, 0, 1])


    def test_count_shared_values_basic(self):
        gridA = [[4, 1], [7, 3], [2, 5]]
        gridB = [[1, 9], [4, 3], [8, 2]]
        self.assertEqual(lab11.count_shared_values(gridA, gridB), 4)

    def test_count_shared_values_none(self):
        gridA = [[1, 2], [3, 4]]
        gridB = [[5, 6], [7, 8]]
        self.assertEqual(lab11.count_shared_values(gridA, gridB), 0)

    def test_count_shared_values_with_duplicates(self):
        gridA = [[1, 1], [2, 2]]
        gridB = [[1, 2], [1, 2]]
        self.assertEqual(lab11.count_shared_values(gridA, gridB), 2)

    def test_count_shared_values_large_overlap(self):
        gridA = [[1, 2, 3], [4, 5, 6]]
        gridB = [[6, 5, 4], [3, 2, 1]]
        self.assertEqual(lab11.count_shared_values(gridA, gridB), 6)


if __name__ == '__main__':
    unittest.main()

