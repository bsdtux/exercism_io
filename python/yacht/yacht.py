"""Yacht Module"""
# Score categories
# Change the values as you see fit
from collections import Counter

YACHT = 12
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice: list, category: int) -> int:
    """Yact Scoring system
    :param dice: List of dice rolls
    :type dice: list
    :param category: Category to check for
    :type category: int
    :returns: Total score
    :rtype: int
    """
    die_set = set(dice)

    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return dice.count(category) * category

    if category == YACHT and len(die_set) == 1:
        return 50

    if (category == CHOICE or (
            category == FULL_HOUSE and has_full_house(dice))):
        return sum(dice)

    if category == FOUR_OF_A_KIND and has_four_of_kind(dice):
        rolls = Counter(dice)
        for die_number, times_rolled in rolls.items():
            if times_rolled >= 4:
                return die_number * 4

    has_little_straight = all([
        die_set == {1, 2, 3, 4, 5}, category == LITTLE_STRAIGHT])
    has_big_straight = all([
        die_set == {2, 3, 4, 5, 6}, category == BIG_STRAIGHT])

    if has_little_straight or has_big_straight:
        return 30

    return 0


def has_full_house(dice: list) -> bool:
    """Checks to see if you have a full house
    :param dice: List of dice rolls
    :type dice: list
    :returns: Success or Failure of a full house
    :rtype: bool
    """
    die_counts = Counter(dice)

    if len(die_counts) != 2:
        return False

    for times_rolled in die_counts.values():
        if times_rolled < 2:
            return False

    return True


def has_four_of_kind(dice: list) -> bool:
    """Checks to see if you have a four of a kind
    :param dice: List of dice rolls
    :type dice: list
    :returns: Success or Failure of four of a kind
    :rtype: bool
    """
    die_counts = Counter(dice)
    is_four_of_kind = False
    for times_rolled in die_counts.values():
        if times_rolled >= 4:
            is_four_of_kind = True

    return is_four_of_kind
