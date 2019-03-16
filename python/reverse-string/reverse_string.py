"""Reverse String Module"""


def reverse(text: str):
    """Reverse text string
    :param text: String to be reversed
    :type text: str
    :returns: Reversed string
    :rtype: str
    """
    if not text:
        return ''

    reversed_string = []
    for character in text:
        reversed_string.insert(0, character)

    return ''.join(reversed_string)
