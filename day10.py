from helpers import *

def getRequiredJoltages(joltages: list[int]) -> list[int]:
    requiredJoltages = []
    for (counter, joltage) in enumerate(joltages):
        if counter > 0:
            if (joltage - joltages[counter - 1] == 3 or
                joltages[counter + 1] - joltage == 3):
                requiredJoltages.append(joltage)
    return requiredJoltages

def getOptionalChunks(allJoltages: list[int], requiredJoltages: list[int]) -> list[list[int]]:
    allChunks = []
    chunk = []
    requiredJoltagesInCurrentChunk = 0
    for joltage in allJoltages:
        if len(chunk) == 0:
            requiredJoltagesInCurrentChunk += 1
            chunk.append(joltage)
        elif joltage not in requiredJoltages:
            chunk.append(joltage)
        elif requiredJoltagesInCurrentChunk == 1 and len(chunk) == 1:
            chunk = []
            chunk.append(joltage)
        else:
            chunk.append(joltage)
            allChunks.append(chunk)
            chunk = []
            requiredJoltagesInCurrentChunk = 0
    return allChunks

def main():
    joltages = [int(line) for line in getFileLines(10)]

    # Part 1

    timer = ExecutionTimer()
    joltages.sort()
    joltages.insert(0, 0) # outlet
    joltages.append(max(joltages) + 3) # device adaptor

    numberOf1JoltGaps = numberOf3JoltGaps = 0
    for (counter, joltage) in enumerate(joltages):
        if counter > 0:
            gapToNext = joltage - joltages[counter - 1]
            if gapToNext == 1:
                numberOf1JoltGaps += 1
            elif gapToNext == 3:
                numberOf3JoltGaps += 1

    result = numberOf1JoltGaps * numberOf3JoltGaps
    print(f"Day 10 part 1 solution: {result}")
    timer.stop()

    # Part 2

    timer = ExecutionTimer()
    requiredJoltages = getRequiredJoltages(joltages)
    optionalChunks = getOptionalChunks(joltages, requiredJoltages)

    # Keys are lengths of chunks, never less than 3
    # Values are the number of ways of spanning that length using only jumps of 1, 2, or 3
    # I calculated them by hand and only went up to 5...
    permutationNumbers = {3: 2, 4: 4, 5: 7}

    part2Result = 1
    for chunk in optionalChunks:
        length = len(chunk)
        try:
            permutations = permutationNumbers[length]
            part2Result *= permutations
        except KeyError:
            print(f"Chunk had {length} elements, which is more than I bargained for...")

    print(f"Day 10 part 2 solution: {part2Result}")
    timer.stop()

if __name__ == "__main__":
    main()