from typing import List

def getFileLines(day: int) -> List[str]:

    """
    Returns the lines of the input for the specified day as a string list,
    stripping newline characters from each one.
    """

    with open('./inputs/{0}.txt'.format(day)) as file:
        return [(line.rstrip('\n')) for line in file]
