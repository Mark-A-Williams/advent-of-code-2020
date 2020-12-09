from helpers import *

class Fine(Exception): pass

def anyInListSumToNumber(number: int, numberList: list[int]) -> bool:
    for x in numberList:
        for y in numberList:
            if x + y == number:
                return True
    return False

def main():
    allNumbers = list(map(lambda x: int(x), getFileLines(9)))

    # Part 1

    timer = ExecutionTimer()

    part1result: int = None
    for (counter, number) in enumerate(allNumbers):
        if (counter >= 25):
            previous25 = allNumbers[counter - 25:counter]
            if not anyInListSumToNumber(number, previous25):
                part1result = number
                break

    if part1result is not None:
        print(f"Day 9 part 1 solution: {part1result}")
    timer.stop()

if __name__ == "__main__":
    main()