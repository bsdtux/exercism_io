"""Unit Test file for hello_world module"""
import unittest

import hello_world

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class HelloWorldTest(unittest.TestCase):
    """Class continaing unit tests for hello world module"""
    def test_hello(self):
        """Test to assert hello_world function return expected result"""
        self.assertEqual(hello_world.hello(), 'Hello, World!')


if __name__ == '__main__':
    unittest.main()
