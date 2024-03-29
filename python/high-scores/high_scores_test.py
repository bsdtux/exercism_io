"""High Scores Test modules"""
import unittest

from high_scores import HighScores

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoreTest(unittest.TestCase):
    """High Scores Test Class"""
    def test_list_of_scores(self):
        """Test the storage of a list of scores"""
        scores = [30, 50, 20, 70]
        expected = [30, 50, 20, 70]
        self.assertEqual(HighScores(scores).scores, expected)

    def test_latest_score(self):
        """Test retrieval of the last score added"""
        scores = [100, 0, 90, 30]
        expected = 30
        self.assertEqual(HighScores(scores).latest(), expected)

    def test_personal_best(self):
        """Test personal best score form a list of 3 scores"""
        scores = [40, 100, 70]
        expected = 100
        self.assertEqual(HighScores(scores).personal_best(), expected)

    def test_personal_top_three_from_a_long_list(self):
        """Test retrieval of high scores from a list with duplicate values"""
        scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
        expected = [100, 90, 70]
        self.assertEqual(HighScores(scores).personal_top_three(), expected)

    def test_personal_top_three_highest_to_lowest(self):
        """Test retrieval of 3 high scores from a list of 3 values"""
        scores = [20, 10, 30]
        expected = [30, 20, 10]
        self.assertEqual(HighScores(scores).personal_top_three(), expected)

    def test_personal_top_three_when_there_is_a_tie(self):
        """Test high scores with duplicate ties for number one"""
        scores = [40, 20, 40, 30]
        expected = [40, 40, 30]
        self.assertEqual(HighScores(scores).personal_top_three(), expected)

    def test_personal_top_three_when_there_are_less_than_3(self):
        """Test high scores with only two values"""
        scores = [30, 70]
        expected = [70, 30]
        self.assertEqual(HighScores(scores).personal_top_three(), expected)

    def test_personal_top_three_when_there_is_only_one(self):
        """Test high scores with only a single value"""
        scores = [40]
        expected = [40]
        self.assertEqual(HighScores(scores).personal_top_three(), expected)


if __name__ == "__main__":
    unittest.main()
