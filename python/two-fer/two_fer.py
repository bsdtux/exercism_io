"""Two Fer module"""


def two_fer(name: str = "you") -> str:
    """Returns a two fer message
    :param name: Name of person that gets something
    :type name: str
    :returns: String with name of person that gets something
    :rtype: str
    """
    return f"One for {name}, one for me."
