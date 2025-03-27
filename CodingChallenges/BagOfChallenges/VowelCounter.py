import unittest

def count_vowels(s):
    count = 0
    for letter in s:
        if(letter.lower() in 'aeiou'):
            count+= 1

    return count

class TestCountVowels(unittest.TestCase):
    
    def test_basic_vowels(self):
        self.assertEqual(count_vowels("Hello World!"), 3)  # e, o, o
        self.assertEqual(count_vowels("Python"), 1)  # o
        self.assertEqual(count_vowels("AEIOU"), 5)  # All vowels
        self.assertEqual(count_vowels("aeiou"), 5)  # All vowels in lowercase

    def test_mixed_case(self):
        self.assertEqual(count_vowels("ApPlE"), 2)  # A, e
        self.assertEqual(count_vowels("QuIeT"), 3)  # u, i, e

    def test_no_vowels(self):
        self.assertEqual(count_vowels("bcdfg"), 0)  # No vowels
        self.assertEqual(count_vowels(""), 0)  # Empty string
        self.assertEqual(count_vowels("123456"), 0)  # Numbers only

    def test_vowels_with_spaces_and_special_chars(self):
        self.assertEqual(count_vowels("I am a programmer!"), 6)  # i, a, a, o, a, e
        self.assertEqual(count_vowels("Why?"), 0)  # 'y' is not a vowel
        self.assertEqual(count_vowels("The quick brown fox jumps!"), 6)  # e, u, i, o, o, u

if __name__ == "__main__":
    unittest.main()
