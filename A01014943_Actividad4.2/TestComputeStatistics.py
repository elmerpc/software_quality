import unittest
import compute_statistics as cs

class TestComputeStatistics(unittest.TestCase):

    def setUp(self):
        self.numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_compute_mean(self):
        result = cs.compute_mean(self.numbers)
        self.assertEqual(result, 5)

    def test_compute_median(self):
        result = cs.compute_median(self.numbers)
        self.assertEqual(result, 5)

    def test_compute_mode(self):
        numbers = [1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
        result = cs.compute_mode(numbers)
        self.assertEqual(result, [2])

    def test_compute_standard_deviation(self):
        result = cs.compute_standard_deviation(self.numbers)
        self.assertAlmostEqual(result, 2.581988897471611, places=7)

    def test_compute_variance(self):
        result = cs.compute_variance(self.numbers)
        self.assertAlmostEqual(result, 6.666666666666667, places=7)

if __name__ == '__main__':
    unittest.main()