from helpers import *
import copy

def applyNextStep(seating: list[list[str]]) -> tuple[bool, list[list[str]]]:
    anyUpdated = False
    updatedSeating = copy.deepcopy(seating)
    for (i, row) in enumerate(seating):
        for (j, seat) in enumerate(row):
            adjacentOccupied = countOfOccupiedAdjacentSeats(seating, i, j)
            if seat == "L" and adjacentOccupied == 0:
                updatedSeating[i][j] = "#"
                anyUpdated = True
            elif seat == "#" and adjacentOccupied >= 4:
                updatedSeating[i][j] = "L"
                anyUpdated = True
    return anyUpdated, updatedSeating


def countOfOccupiedAdjacentSeats(seating: list[list[str]], rowIndex: int, seatIndex: int) -> int:
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


def main():
    seating = [list(line) for line in getFileLines(11)]
    # seating = [list(line) for line in [
    #     "L.LL.LL.LL","LLLLLLL.LL","L.L.L..L..","LLLL.LL.LL","L.LL.LL.LL","L.LLLLL.LL","..L.L.....","LLLLLLLLLL","L.LLLLLL.L","L.LLLLL.LL"
    # ]]

    anyUpdated = True
    updatedSeating: list[list[str]] = []
    while anyUpdated:
        anyUpdated, updatedSeating = applyNextStep(seating)
        print(anyUpdated)
        seating = updatedSeating.copy()

    occupiedSeats = 0
    for row in updatedSeating:
        for seat in row:
            if seat == "#":
                occupiedSeats += 1

    print(occupiedSeats)



if __name__ == "__main__":
    main()