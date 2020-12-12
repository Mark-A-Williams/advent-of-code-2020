from helpers import *
from typing import Callable
import copy

def applyNextStep(
    seating: list[list[str]],
    occupancyCountFunction: Callable[[list[list[str]]], int],
    maximumAdjacencyTolerance: int) -> tuple[bool, list[list[str]]]:
    
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

def getIsOccupiedSeatInDirection(
    seating: list[list[str]],
    rowIndex: int,
    seatIndex: int,
    rowStep: int,
    seatStep: int) -> bool:

    numberOfRows = len(seating)
    rowLength = len(seating[0])

    while True:
        rowIndex += rowStep
        seatIndex += seatStep
        if (0 <= rowIndex < numberOfRows) and (0 <= seatIndex < rowLength):
            nextSeat = seating[rowIndex][seatIndex]
            if nextSeat == "#":
                return True
            elif nextSeat == "L":
                return False
        else:
            return False

def lineOfSightCount(seating: list[list[str]], rowIndex: int, seatIndex: int) -> int:
    count = 0
    for rowStep in [-1, 0, 1]:
        for seatStep in [-1, 0, 1]:
            if ((rowStep != 0 or seatStep != 0)
                and getIsOccupiedSeatInDirection(seating, rowIndex, seatIndex, rowStep, seatStep)):
                count += 1
    return count

def getFinalOccupiedSeats(seating: list[list[str]], callbackFunc: Callable[[list[list[str]]], int], tolerance: int) -> int:
    anyUpdated = True
    updatedSeating: list[list[str]] = []

    while anyUpdated:
        anyUpdated, updatedSeating = applyNextStep(seating, callbackFunc, tolerance)
        seating = updatedSeating

    result = 0
    for row in updatedSeating:
        for seat in row:
            if seat == "#":
                result += 1
    return result

def main():
    seating = [list(line) for line in getFileLines(11)]

    # Part 1

    timer = ExecutionTimer()
    part1Result = getFinalOccupiedSeats(seating, simpleAdjacencyCount, 4)
    print(f"Day 11 part 1 solution: {part1Result}")
    timer.stop()

    # Part 2

    timer = ExecutionTimer()
    part2Result = getFinalOccupiedSeats(seating, lineOfSightCount, 5)
    print(f"Day 11 part 2 solution: {part2Result}")
    timer.stop()

if __name__ == "__main__":
    main()