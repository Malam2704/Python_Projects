import unittest

def is_anagram(str1, str2):
    set1 = {}
    set2 = {}
    str1new = ""
    str2new = ""
    for i in str1:
        if(i.isalnum()):
            str1new += i.lower()
    for i in str2:
        if(i.isalnum()):
            str2new += i.lower()

    str1 = str1new
    str2 = str2new

    for i in str1:
        if(i in set1):
            set1[i] = set1[i] + 1
        else:
            set1[i] = 1
    for j in str2:
        if(j in set2):
            set2[j] = set2[j] + 1
        else:
            set2[j] = 1

    print(set1, set2, set1 == set2)
    return set1==set2

class TestIsAnagram(unittest.TestCase):
    
    def test_valid_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("elbow", "below"))
        self.assertTrue(is_anagram("dusty", "study"))
        self.assertTrue(is_anagram("night", "thing"))
        self.assertTrue(is_anagram("astronomer", "moon starer"))
        self.assertTrue(is_anagram("The eyes", "They see"))
        self.assertTrue(is_anagram("School master", "The classroom"))

    def test_invalid_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("openai", "aiopened"))  # Same letters but different frequency/order
        self.assertFalse(is_anagram("anagram", "nagaramm"))  # Extra 'm'
        self.assertFalse(is_anagram("rat", "car"))

    def test_edge_cases(self):
        self.assertTrue(is_anagram("", ""))  # Empty strings
        self.assertTrue(is_anagram("a", "a"))  # Single character, same letter
        self.assertFalse(is_anagram("a", "b"))  # Single character, different letters
        self.assertTrue(is_anagram("123", "231"))  # Numbers treated as characters
        self.assertFalse(is_anagram("123", "3214"))  # Different lengths

if __name__ == "__main__":
    unittest.main()