from helpers import *

def numberOfTreesHit(movesRight: int, movesDown: int, pointsPerLine: int, lines: list) -> int:
    treesHit = 0
    for (counter, line) in enumerate(lines):
        if (counter % movesDown == 0):
            positionToCheck = int((movesRight * counter / movesDown) % pointsPerLine)
            if (line[positionToCheck] == '#'):
                treesHit += 1
    return treesHit    

def main():
    lines = getFileLines(3)
    pointsPerLine = len(lines[0])

    # Part 1
    timer = executionTimer()
    part1Solution = numberOfTreesHit(3, 1, pointsPerLine, lines)
    print('Day 3 part 1 solution: {0}'.format(part1Solution))
    timer.stopTimer()

    # Part 2
    timer = executionTimer()

    part2Solution = (numberOfTreesHit(1, 1, pointsPerLine, lines)
        * numberOfTreesHit(3, 1, pointsPerLine, lines)
        * numberOfTreesHit(5, 1, pointsPerLine, lines)
        * numberOfTreesHit(7, 1, pointsPerLine, lines)
        * numberOfTreesHit(1, 2, pointsPerLine, lines))

    print('Day 3 part 2 solution: {0}'.format(part2Solution))
    timer.stopTimer()

if (__name__ == '__main__'):
    main()