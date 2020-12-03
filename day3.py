from executionTimer import executionTimer

# Part 1

timer = executionTimer()

with open('./inputs/3.txt') as file:
    lines = [(line.rstrip('\n')) for line in file]

pointsPerLine = len(lines[0])

treesHit = 0
for (counter, line) in enumerate(lines):
    positionToCheck = (3 * counter) % pointsPerLine
    if (line[positionToCheck] == '#'):
        treesHit += 1

print(treesHit)
timer.stopTimer()