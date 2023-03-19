import unittest

from epic import find_substring, find_substring_bruteforce

class TestSubstring(unittest.TestCase):

    def test_simple(self):
        case = 'abc'
        first, second = find_substring(case)

        self.assertEqual(first, 'ab')
        self.assertEqual(second, 'abc')
        
        first, second = find_substring_bruteforce(case)

        self.assertEqual(first, 'ab')
        self.assertEqual(second, 'abc')

    def test_longer(self):
        case = 'abcaauiz'
        first, second = find_substring(case)

        self.assertEqual(first, 'aauiz')
        self.assertEqual(second, 'uiz')

        first, second = find_substring_bruteforce(case)

        self.assertEqual(first, 'aauiz')
        self.assertEqual(second, 'uiz')

    def test_no_a_or_u(self):
        case = 'cmcreqiqnccznzpeirqrieoqipqpmcznkjfkqwr'

        first, second = find_substring(case)

        self.assertEqual(first, 'eir')
        self.assertEqual(second, 'oqipqpmcznkjfkqwr')

        first, second = find_substring_bruteforce(case)

        self.assertEqual(first, 'eir')
        self.assertEqual(second, 'oqipqpmcznkjfkqwr')

if __name__ == "__main__":
    unittest.main()