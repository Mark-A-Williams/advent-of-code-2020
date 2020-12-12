from helpers import *
from typing import List

class Fine(Exception): pass

def anyInListSumToNumber(number: int, numberList: List[int]) -> bool:
    for x in numberList:
        for y in numberList:
            if x + y == number:
                return True
    return False

def tryFindListAddingToNumberStartingAtIndex(
    index: int,
    target: int,
    allNumbers: List[int]) -> List[int]:

    sum = 0
    listSoFar: List[int] = []
    nextIndex = index

    while sum < target:
        nextNumber = allNumbers[nextIndex]
        listSoFar.append(nextNumber)
        sum += nextNumber
        if sum == target:
            return listSoFar
        nextIndex += 1
    return None

def main():
    allNumbers = list(map(lambda x: int(x), getFileLines(9)))

    # Part 1

    timer = ExecutionTimer()

    part1result: int = None
    for (i, number) in enumerate(allNumbers):
        if (i >= 25):
            previous25 = allNumbers[i - 25 : i]
            if not anyInListSumToNumber(number, previous25):
                part1result = number
                break

    if part1result is not None:
        print(f"Day 9 part 1 solution: {part1result}")
    timer.stop()

    # Part 2

    succeedingList: List[int] = None
    for i in range(len(allNumbers)):
        succeedingList = tryFindListAddingToNumberStartingAtIndex(i, part1result, allNumbers)
        if succeedingList is not None:
            break

    timer = ExecutionTimer()
    if succeedingList is not None:
        part2result = min(succeedingList) + max(succeedingList)
        print(f"Day 9 part 2 solution: {part2result}")
        timer.stop()


if __name__ == "__main__":
    main()