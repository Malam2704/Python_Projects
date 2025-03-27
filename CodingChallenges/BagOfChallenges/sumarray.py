import unittest

def sum_of_array(arr):
    sum = 0
    for num in arr:
        sum += num
    return sum

class TestSumOfArray(unittest.TestCase):
    
    def test_non_empty_array(self):
        self.assertEqual(sum_of_array([1, 2, 3, 4, 5]), 15)
        
    def test_negative_numbers(self):
        self.assertEqual(sum_of_array([-1, -2, -3, -4, -5]), -15)

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_array([1, -2, 3, -4, 5]), 3)

    def test_empty_array(self):
        self.assertEqual(sum_of_array([]), 0)

    def test_single_element(self):
        self.assertEqual(sum_of_array([7]), 7)

    def test_large_numbers(self):
        self.assertEqual(sum_of_array([1000000000, 2000000000, 3000000000]), 6000000000)

    def test_all_zeros(self):
        self.assertEqual(sum_of_array([0, 0, 0, 0, 0]), 0)

    def test_large_and_small(self):
        self.assertEqual(sum_of_array([100000, -1]), 99999)

    def test_repeating_elements(self):
        self.assertEqual(sum_of_array([1, 1, 1, 1, 1]), 5)

    def test_large_array(self):
        self.assertEqual(sum_of_array([i for i in range(1, 1001)]), 500500)

if __name__ == "__main__":
    unittest.main()
