"""Yacht Test Module"""

import unittest

import yacht
from yacht import score

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0


class YachtTest(unittest.TestCase):  # pylint: disable=R0904
    """Yacht Test class"""
    def test_yacht(self):
        """Test for YACHT"""
        self.assertEqual(score([5, 5, 5, 5, 5], yacht.YACHT), 50)

    def test_not_yacht(self):
        """Test for not a YACHT"""
        self.assertEqual(score([1, 3, 3, 2, 5], yacht.YACHT), 0)

    def test_ones(self):
        """Test scores for ONES"""
        self.assertEqual(score([1, 1, 1, 3, 5], yacht.ONES), 3)

    def test_ones_out_of_order(self):
        """Test scores for ONES in random order"""
        self.assertEqual(score([3, 1, 1, 5, 1], yacht.ONES), 3)

    def test_no_ones(self):
        """TEST of ONES with none in roll"""
        self.assertEqual(score([4, 3, 6, 5, 5], yacht.ONES), 0)

    def test_twos(self):
        """test twos"""
        self.assertEqual(score([2, 3, 4, 5, 6], yacht.TWOS), 2)

    def test_fours(self):
        """test fours"""
        self.assertEqual(score([1, 4, 1, 4, 1], yacht.FOURS), 8)

    def test_yacht_counted_as_threes(self):
        """test yacht"""
        self.assertEqual(score([3, 3, 3, 3, 3], yacht.THREES), 15)

    def test_yacht_of_threes_counted_as_fives(self):
        """test 5 3 as fives"""
        self.assertEqual(score([3, 3, 3, 3, 3], yacht.FIVES), 0)

    def test_sixes(self):
        """test sixes"""
        self.assertEqual(score([2, 3, 4, 5, 6], yacht.SIXES), 6)

    def test_full_house_two_small_three_big(self):
        """test  full house"""
        self.assertEqual(score([2, 2, 4, 4, 4], yacht.FULL_HOUSE), 16)

    def test_full_house_three_small_two_big(self):
        """test full house"""
        self.assertEqual(score([5, 3, 3, 5, 3], yacht.FULL_HOUSE), 19)

    def test_two_pair_is_not_a_full_house(self):
        """test invalid full house"""
        self.assertEqual(score([2, 2, 4, 4, 5], yacht.FULL_HOUSE), 0)

    def test_four_of_a_kind_is_not_a_full_house(self):
        """test four of a kind as full house"""
        self.assertEqual(score([1, 4, 4, 4, 4], yacht.FULL_HOUSE), 0)

    def test_yacht_is_not_a_full_house(self):
        """test yacht as a full house"""
        self.assertEqual(score([2, 2, 2, 2, 2], yacht.FULL_HOUSE), 0)

    def test_four_of_a_kind(self):
        """test four of a kind"""
        self.assertEqual(score([6, 6, 4, 6, 6], yacht.FOUR_OF_A_KIND), 24)

    def test_yacht_can_be_scored_as_four_of_a_kind(self):
        """test four of a kind as yacht"""
        self.assertEqual(score([3, 3, 3, 3, 3], yacht.FOUR_OF_A_KIND), 12)

    def test_full_house_is_not_four_of_a_kind(self):
        """test invalid four of a kind"""
        self.assertEqual(score([3, 5, 4, 1, 2], yacht.FOUR_OF_A_KIND), 0)

    def test_little_straight(self):
        """test valid little straight"""
        self.assertEqual(score([3, 5, 4, 1, 2], yacht.LITTLE_STRAIGHT), 30)

    def test_little_straight_as_big_straight(self):
        """test little straight as big straight"""
        self.assertEqual(score([1, 2, 3, 4, 5], yacht.BIG_STRAIGHT), 0)

    def test_four_in_order_but_not_a_little_straight(self):
        """test invalid little straight"""
        self.assertEqual(score([1, 1, 2, 3, 4], yacht.LITTLE_STRAIGHT), 0)

    def test_no_pairs_but_not_a_little_straight(self):
        """test invalid little straight"""
        self.assertEqual(score([1, 2, 3, 4, 6], yacht.LITTLE_STRAIGHT), 0)

    def test_min_1_max_5_but_not_a_little_straight(self):
        """test invalid little straight"""
        self.assertEqual(score([1, 1, 3, 4, 5], yacht.LITTLE_STRAIGHT), 0)

    def test_big_straight(self):
        """test big straigh"""
        self.assertEqual(score([4, 6, 2, 5, 3], yacht.BIG_STRAIGHT), 30)

    def test_big_straight_as_little_straight(self):
        """test big straight as little straight"""
        self.assertEqual(score([6, 5, 4, 3, 2], yacht.LITTLE_STRAIGHT), 0)

    def test_choice(self):
        """Test yacht choice random"""
        self.assertEqual(score([3, 3, 5, 6, 6], yacht.CHOICE), 23)

    def test_yacht_as_choice(self):
        """Test yacht choice"""
        self.assertEqual(score([2, 2, 2, 2, 2], yacht.CHOICE), 10)


if __name__ == '__main__':
    unittest.main()
