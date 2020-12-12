from helpers import *
from typing import List

def parsePassToBinary(boardingPass: str) -> int:
    return int(boardingPass
        .replace("F", "0")
        .replace("L", "0")
        .replace("B", "1")
        .replace("R", "1"), 2)

def main():

    # Part 1

    boardingPasses = getFileLines(5)
    seatIds: List[int] = []

    timer = ExecutionTimer()

    for bp in boardingPasses:
        seatIds.append(parsePassToBinary(bp))

    print('Day 5 part 1 solution: {0}'.format(max(seatIds)))
    timer.stop()

    # Part 2
    
    timer = ExecutionTimer()
    seatIds.sort()

    for (counter, seatId) in enumerate(seatIds):
        if (seatId == seatIds[counter - 1] + 2):
            print('Day 5 part 2 solution: {0}'.format(seatId - 1))
            break

    timer.stop()

if __name__ == "__main__":
    main()