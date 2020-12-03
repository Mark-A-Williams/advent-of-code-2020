from executionTimer import executionTimer

def numberOfTreesHit(movesRight: int, movesDown: int, pointsPerLine: int) -> int:
    treesHit = 0
    for (counter, line) in enumerate(lines):
        if (counter % movesDown == 0):
            positionToCheck = int((movesRight * counter / movesDown) % pointsPerLine)
            if (line[positionToCheck] == '#'):
                treesHit += 1
    return treesHit    

# Part 1

timer = executionTimer()

with open('./inputs/3.txt') as file:
    lines = [(line.rstrip('\n')) for line in file]

pointsPerLine = len(lines[0])

part1Solution = numberOfTreesHit(3, 1, pointsPerLine)
print('Day 3 part 1 solution: {0}'.format(part1Solution))
timer.stopTimer()

# Part 2

timer = executionTimer()

part2SolutionComponents = [
    numberOfTreesHit(1, 1, pointsPerLine),
    numberOfTreesHit(3, 1, pointsPerLine),
    numberOfTreesHit(5, 1, pointsPerLine),
    numberOfTreesHit(7, 1, pointsPerLine),
    numberOfTreesHit(1, 2, pointsPerLine)
]

part2Solution = 1
for component in part2SolutionComponents:
    part2Solution *= component

print('Day 3 part 2 solution: {0}'.format(part2Solution))
timer.stopTimer()