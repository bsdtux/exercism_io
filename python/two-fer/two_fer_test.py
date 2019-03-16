"""Unit Test file for two-fer module"""

import unittest

from two_fer import two_fer

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.2.0


class TwoFerTest(unittest.TestCase):
    """Class continaing unit tests for two fer module"""
    def test_no_name_given(self):
        """Test no name given to two_fer function"""
        self.assertEqual(two_fer(), 'One for you, one for me.')

    def test_a_name_given(self):
        """Test giving Parameter Alice to two_fer"""
        self.assertEqual(two_fer("Alice"), "One for Alice, one for me.")

    def test_another_name_given(self):
        """Test giving Parameter Bob to two_fer"""
        self.assertEqual(two_fer("Bob"), "One for Bob, one for me.")


if __name__ == '__main__':
    unittest.main()
