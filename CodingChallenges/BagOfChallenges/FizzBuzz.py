import unittest
def fizzbuzz(num):
    return_array = []
    for i in range(1, num+1):
        if(i % 5 == 0 and i % 3 == 0):
            return_array.append("FizzBuzz")
        elif(i% 5 == 0):
            return_array.append('Buzz')
        elif(i% 3 == 0):
            return_array.append('Fizz')
        else:
            return_array.append(str(i))
    return return_array

class TestFizzBuzz(unittest.TestCase):
    
    def test_small_numbers(self):
        self.assertEqual(fizzbuzz(1), ["1"])
        self.assertEqual(fizzbuzz(2), ["1", "2"])
        self.assertEqual(fizzbuzz(3), ["1", "2", "Fizz"])
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_fizzbuzz_sequence(self):
        self.assertEqual(fizzbuzz(15), [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz"
        ])

    def test_negative_and_zero(self):
        self.assertEqual(fizzbuzz(0), [])  # Edge case: Zero
        self.assertEqual(fizzbuzz(-5), [])  # Edge case: Negative input

    def test_exact_fizzbuzz_numbers(self):
        self.assertEqual(fizzbuzz(3), ["1", "2", "Fizz"])
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])
        self.assertEqual(fizzbuzz(15)[-1], "FizzBuzz")  # Last item should be "FizzBuzz"

if __name__ == "__main__":
    unittest.main()
