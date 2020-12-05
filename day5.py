from helpers import *
    
def parsePassToBinary(boardingPass: str) -> int:
    return int(boardingPass
        .replace("F", "0")
        .replace("L", "0")
        .replace("B", "1")
        .replace("R", "1"), 2)

def main():

    # Part 1

    boardingPasses = getFileLines(5)
    seatIds: list[int] = []

    timer = executionTimer()

    for bp in boardingPasses:
        seatIds.append(parsePassToBinary(bp))

    print('Day 5 part 1 solution: {0}'.format(max(seatIds)))
    timer.stopTimer()

    # Part 2
    
    timer = executionTimer()
    seatIds.sort()

    for (counter, seatId) in enumerate(seatIds):
        if (seatId == seatIds[counter - 1] + 2):
            print('Day 5 part 2 solution: {0}'.format(seatId - 1))
            break

    timer.stopTimer()

if __name__ == "__main__":
    main()