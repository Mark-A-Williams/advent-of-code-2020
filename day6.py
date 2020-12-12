from helpers import *
from typing import List

def getCountForGroup(group: List[str]) -> int:
    lettersInEveryone: List[str] = []
    for (i, person) in enumerate(group):
        if (i == 0):
            for letter in person:
                lettersInEveryone.append(letter)
        else:
            lettersStillInEveryone: List[str] = lettersInEveryone.copy()
            for letter in lettersInEveryone:
                if letter not in person:
                    lettersStillInEveryone.remove(letter)
                    if len(lettersStillInEveryone) == 0:
                        return 0
                    else:
                        lettersInEveryone = lettersStillInEveryone.copy()

    return len(lettersInEveryone)

def main():
    with open('./inputs/6.txt') as file:
        groups: List[str] = file.read().split('\n\n')

    # Part 1

    timer = ExecutionTimer()
    part1Solution = 0
    compressedGroups = [group.replace("\n", "") for group in groups]

    for group in compressedGroups:
        uniqueCharacters: List[str] = []
        for char in group:
            if not (char in uniqueCharacters):
                uniqueCharacters.append(char)
        part1Solution += len(uniqueCharacters)

    print('Day 6 part 1 solution: {0}'.format(part1Solution))
    timer.stop()

    # Part 2

    timer = ExecutionTimer()
    structuredGroups = [group.split("\n") for group in groups]

    part2Solution = 0
    for group in structuredGroups:
        part2Solution += getCountForGroup(group)

    print('Day 6 part 2 solution: {0}'.format(part2Solution))
    timer.stop()

if __name__ == "__main__":
    main()