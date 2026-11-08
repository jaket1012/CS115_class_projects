import unittest
import time
import random
import hw6

class TestParseFile(unittest.TestCase):

    def test_parse_file_valid_example(self):
        grid = hw6.parse_file("grids/example.txt")
        expected = [
            [1, 5, 7, 1],
            [3, 6, 4, 2],
            [7, 2, 3, 5],
        ]
        self.assertEqual(grid, expected)

    def test_parse_file_invalid_missing_dimensions(self):
        """not listing the dimensions at the top of the file should raise a ValueError."""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_missing_dimensions.txt")

    def test_parse_file_invalid_wrong_dimension_values(self):
        """listing too few integers should raise a ValueError."""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_wrong_dimension_values.txt")

    def test_parse_file_invalid_row_too_short(self):
        """a row containing fewer than m values should raise ValueError"""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_row_too_short.txt")

    def test_parse_file_invalid_too_few_rows(self):
        """containing fewer than n rows should raise a ValueError"""
        with self.assertRaises(ValueError):
            hw6.parse_file("grids/invalid_too_few_rows.txt")

    def test_parse_file_multidigit_dimensions(self):
        grid_path = "grids/grid_15x20.txt"
        grid = hw6.parse_file(grid_path)
        self.assertEqual(len(grid), 15)
        for row in grid:
            self.assertEqual(len(row), 20)

class TestDistancesFrom(unittest.TestCase):

    def test_distances_from_simple_grid(self):
        grid = [
            [1, 2, 4],
            [5, 3, 7],
            [10, 5, 6],
        ]

        d = hw6.distances_from(grid)

        expected = [
            [1, 3, 7],
            [6, 6, 13],
            [16, 6+5, 11+6],
        ]

        self.assertEqual(d, expected)

    def test_distances_from_rectangular_grid(self):
        grid = [
            [2, 9, 1, 1],
            [1, 2, 1, 1],
        ]
        d = hw6.distances_from(grid)

        expected = [
            [2, 11, 12, 13],
            [3, 5, 6, 7],
        ]

        self.assertEqual(d, expected)



    def test_efficient_distance_from_15x20_grid_under_one_second(self):
        """distances_from should finish on a 15 x 20 grid in < 1s."""
        grid_path = "grids/grid_15x20.txt"
        grid = hw6.parse_file(grid_path)
        start_time = time.time()
        _ = hw6.distances_from(grid)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1)

    def test_efficient_distance_from_random_medium_grid_under_one_second(self):
        grid = [[random.randint(1,10)]*10 for _ in range(10)]
        start_time = time.time()
        _ = hw6.distances_from(grid)
        end_time = time.time()
        self.assertLess(end_time - start_time, 1)

class TestShortestPath(unittest.TestCase):

    def test_shortest_path_simple_2x2(self):
        dists = [
            [0, 1],
            [1, 2],
        ]
        # path should go (1,1) -> (1,0) -> (0,0) OR
        #                     -> (0,1) -> (0,0)
        result = hw6.shortest_path(dists, (1,1))
        self.assertEqual(result[0], (1,1))
        self.assertEqual(result[-1], (0,0))
        # Multiple potential paaths, so we don't check 1
        self.assertEqual(len(result), 3)

    def test_shortest_path_example_from_handout(self):
        """
        example from the handout
        """
        dists = [
            [1, 6, 13, 14],
            [4, 10, 14, 16],
            [11, 12, 15, 20],
        ]

        expected = [(3,2), (2,2), (1,2), (1,1), (0,1), (0,0)]
        result = hw6.shortest_path(dists, (3,2))
        self.assertEqual(result, expected)

    def test_shortest_path_4x4(self):
        dists = [
            [0, 1, 2, 3],
            [1, 2, 9, 4],
            [2, 3, 4, 5],
            [3, 4, 5, 6],
        ]
        expected = [
            (3,3), (3,2), (3,1), (3,0),
            (2,0), (1,0), (0,0)
        ]
        result = hw6.shortest_path(dists, (3,3))
        try:
            self.assertEqual(result, expected, "returned path doesn't match expected.")
        except AssertionError:
            costs = map(lambda pair: dists[pair[1]][pair[0]], result)
            expected_cost = 21
            self.assertEqual(sum(costs), expected_cost, f"returned path {result} does not match expected cost: {expected_cost}.")



if __name__ == "__main__":
    unittest.main()
