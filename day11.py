from helpers import *
from typing import Callable
import copy

def applyNextStep(
    seating: list[list[str]],
    occupancyCountFunction: Callable[[list[list[str]]], int],
    maximumAdjacencyTolerance: int) -> tuple[bool, list[list[str]]]:
    
    print(occupancyCountFunction.__name__)
    anyUpdated = False
    updatedSeating = copy.deepcopy(seating)
    for (i, row) in enumerate(seating):
        for (j, seat) in enumerate(row):
            adjacentOccupied = occupancyCountFunction(seating, i, j)
            if seat == "L" and adjacentOccupied == 0:
                updatedSeating[i][j] = "#"
                anyUpdated = True
            elif seat == "#" and adjacentOccupied >= maximumAdjacencyTolerance:
                updatedSeating[i][j] = "L"
                anyUpdated = True
    return anyUpdated, updatedSeating

def simpleAdjacencyCount(seating: list[list[str]], rowIndex: int, seatIndex: int) -> int:
    numberOfRows = len(seating)
    rowLength = len(seating[0])
    adjacentSeats = []

    if seatIndex > 0:
        adjacentSeats.append(seating[rowIndex][seatIndex - 1])
    if seatIndex < rowLength - 1:
        adjacentSeats.append(seating[rowIndex][seatIndex + 1])
    if rowIndex > 0:
        adjacentSeats.append(seating[rowIndex - 1][seatIndex])
        if seatIndex > 0:
            adjacentSeats.append(seating[rowIndex - 1][seatIndex - 1])
        if seatIndex < rowLength - 1:
            adjacentSeats.append(seating[rowIndex - 1][seatIndex + 1])
    if rowIndex < numberOfRows - 1:
        adjacentSeats.append(seating[rowIndex + 1][seatIndex])
        if seatIndex > 0:
            adjacentSeats.append(seating[rowIndex + 1][seatIndex - 1])
        if seatIndex < rowLength - 1:
            adjacentSeats.append(seating[rowIndex + 1][seatIndex + 1])

    return adjacentSeats.count("#")

def lineOfSightCount(seating: list[list[str]], rowIndex: int, seatIndex: int) -> int:
    return 0

def getFinalOccupiedSeats(seating: list[list[str]], callbackFunc: Callable[[list[list[str]]], int], tolerance: int) -> int:
    anyUpdated = True
    updatedSeating: list[list[str]] = []

    while anyUpdated:
        anyUpdated, updatedSeating = applyNextStep(seating, callbackFunc, 4)
        seating = updatedSeating

    result = 0
    for row in updatedSeating:
        for seat in row:
            if seat == "#":
                result += 1
    return result

def main():
    seating = [list(line) for line in getFileLines(11)]
    # seating = [list(line) for line in [
    #     "L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"
    # ]]

    # Part 1

    timer = ExecutionTimer()
    part1Result = getFinalOccupiedSeats(copy.deepcopy(seating), simpleAdjacencyCount, 4)
    print(f"Day 11 part 1 solution: {part1Result}")
    timer.stop()

    # Part 2

    # seating = [list(line) for line in [
    #     "L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"
    # ]]

    timer = ExecutionTimer()
    part2Result = getFinalOccupiedSeats(copy.deepcopy(seating), lineOfSightCount, 5)
    print(f"Day 11 part 2 solution: {part2Result}")
    timer.stop()

if __name__ == "__main__":
    main()