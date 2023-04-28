"""High Scores Module"""


class HighScores(object):  # pylint: disable=useless-object-inheritance
    """Represents HighScores from a video game"""
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """Retrieves the last score"""
        return self.scores[-1]

    def personal_best(self):
        """Retrieve the best score"""
        return sorted(self.scores, reverse=True)[0]

    def personal_top_three(self):
        """Retrieve the top 3 scores"""
        return sorted(self.scores, reverse=True)[:3]
