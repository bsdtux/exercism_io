"""Unit Test file for reverse string module"""
import unittest

from reverse_string import reverse

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class ReverseStringTest(unittest.TestCase):
    """Class continaing unit tests for two fer module"""
    def test_empty_string(self):
        """Unit test for testing empty string"""
        self.assertEqual(reverse(''), '')

    def test_a_word(self):
        """Unit test for reversing string robot"""
        self.assertEqual(reverse('robot'), 'tobor')

    def test_a_capitalized_word(self):
        """Unit test for reversing string Ramen"""
        self.assertEqual(reverse('Ramen'), 'nemaR')

    def test_a_sentence_with_punctuation(self):
        """Unit test for reversing string I'm hungry!'"""
        self.assertEqual(reverse('I\'m hungry!'), '!yrgnuh m\'I')

    def test_a_palindrome(self):
        """Unit test for reversing string racecar"""
        self.assertEqual(reverse('racecar'), 'racecar')


if __name__ == '__main__':
    unittest.main()
