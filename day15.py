from helpers import *
from typing import List, Dict

def getNthNumber(n: int):
    input = [0,20,7,16,1,18,15]

    numbers: List[int] = []
    index = 0
    lastSpokenNumber = input[0]
    seenNumbers: Dict[int, List[int]] = {}

    while index < n:
        if index < len(input):
            nextNumber = input[index]
        elif len(seenNumbers[lastSpokenNumber]) == 1:
            nextNumber = 0
        else:
            nextNumber = seenNumbers[lastSpokenNumber][-1] - seenNumbers[lastSpokenNumber][-2]

        if nextNumber not in seenNumbers:
            seenNumbers[nextNumber] = []
        seenNumbers[nextNumber].append(index)

        numbers.append(nextNumber)
        lastSpokenNumber = nextNumber
        index += 1
    return numbers[-1]


def main():
    # Part 1
    timer = ExecutionTimer()
    part1Result = getNthNumber(2020)
    print(f"Day 15 part 1 solution: {part1Result}")
    timer.stop()

    # Part 2
    timer = ExecutionTimer()
    part1Result = getNthNumber(30000000)
    print(f"Day 15 part 2 solution: {part1Result}")
    timer.stop()

if __name__ == "__main__":
    main()