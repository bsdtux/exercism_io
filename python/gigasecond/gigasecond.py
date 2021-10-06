"""Gigasecond Module"""
from datetime import timedelta


def add_gigasecond(moment):
    """Finds when a person has reached a gigasecond
    :param moment: Starting Moment in time
    :type moment: Datetime
    :returns: Exact Moment a person has reached a gigasecond
    :rtype: Datetime
    """
    gigasecond = 1000000000

    return moment + timedelta(seconds=gigasecond)
