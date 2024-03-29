"""Gigasecond Test Module"""
import unittest
from datetime import datetime

from gigasecond import add_gigasecond

# Tests adapted from `problem-specifications//canonical-data.json` @ v2.0.0


class GigasecondTest(unittest.TestCase):
    """Gigasecond Testing Class"""
    def test_date_only_specification_of_time(self):
        """Test giga second based on date only"""
        self.assertEqual(
            add_gigasecond(datetime(2011, 4, 25)),
            datetime(2043, 1, 1, 1, 46, 40))

    def test_another_date_only_specification_of_time(self):
        """Test giga second based on date only"""
        self.assertEqual(
            add_gigasecond(datetime(1977, 6, 13)),
            datetime(2009, 2, 19, 1, 46, 40))

    def test_one_more_date_only_specification_of_time(self):
        """Test gigasecond based on date only"""
        self.assertEqual(
            add_gigasecond(datetime(1959, 7, 19)),
            datetime(1991, 3, 27, 1, 46, 40))

    def test_full_time_specified(self):
        """Test gigasecond with full date time"""
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 22, 0, 0)),
            datetime(2046, 10, 2, 23, 46, 40))

    def test_full_time_with_day_roll_over(self):
        """Test gigaseond with day roll over"""
        self.assertEqual(
            add_gigasecond(datetime(2015, 1, 24, 23, 59, 59)),
            datetime(2046, 10, 3, 1, 46, 39))

    def test_yourself(self):
        """Test my birthday :) """
        # customize this to test your birthday and find your gigasecond date:
        your_birthday = datetime(1983, 2, 14)
        your_gigasecond = datetime(2014, 10, 23, 1, 46, 40)

        self.assertEqual(add_gigasecond(your_birthday), your_gigasecond)


if __name__ == '__main__':
    unittest.main()
