from helpers import *
from operator import add
from typing import List
import numpy as np

def getUpdatedPosition(startCoords: List[int], direction: str, distance: int) -> List[int]:
    if len(startCoords) != 2:
        raise Exception(f"Invalid start coords: {startCoords}")

    movementVector: List[int] = []
    if direction == "E":
        movementVector = [distance, 0]
    if direction == "W":
        movementVector = [-distance, 0]
    if direction == "N":
        movementVector = [0, distance]
    if direction == "S":
        movementVector = [0, -distance]

    return list(map(add, movementVector, startCoords))

def getUpdatedDirection(currentDirection: str, turn: str, turnAngle: int) -> str:
    directions = ["N", "E", "S", "W"]
    index = directions.index(currentDirection)
    if turn == "L":
        return directions[(index - turnAngle // 90) % 4]
    elif turn == "R":
        return directions[(index + turnAngle // 90) % 4]
    else:
        raise Exception("Invalid turn")

def getRotatedWaypointPosition(waypointCoords: List[int], shipCoords: List[int], code: str, value: int) -> List[int]:
    if len(waypointCoords) != 2 or len(shipCoords) != 2:
        raise Exception("Invalid turn")

    newVectorToWaypoint: List[int] = []
    if value == 180:
        newVectorToWaypoint = list(map(lambda x: x * -1, waypointCoords))
    elif value == 270:
        value = 90
        newCode: str = None
        if code == "L":
            newCode = "R"
        if code == "R":
            newCode = "L"
        newVectorToWaypoint = getRotatedWaypointPosition(waypointCoords, shipCoords, newCode, value)
    elif value == 90:
        if code == "L":
            newVectorToWaypoint = [- waypointCoords[1], waypointCoords[0]]
        elif code == "R":
            newVectorToWaypoint = [waypointCoords[1], - waypointCoords[0]]
    
    return newVectorToWaypoint

def moveShipTowardWaypoint(waypointCoords: List[int], shipCoords: List[int], value: int) -> List[int]:
    movementVector = list(map(lambda x: x * value, waypointCoords))
    return list(map(add, movementVector, shipCoords))

def main():
    instructions = getFileLines(12)

    # Part 1

    timer = ExecutionTimer()
    currentDirection = "E"
    coords = [0, 0]

    for instruction in instructions:
        code, value = instruction[0], int(instruction[1:])
        if code in ["L", "R"]:
            currentDirection = getUpdatedDirection(currentDirection, code, value)
        elif code == "F":
            coords = getUpdatedPosition(coords, currentDirection, value)
        elif code in ["N", "E", "S", "W"]:
            coords = getUpdatedPosition(coords, code, value)
        else:
            raise Exception("Invalid instruction")

    part1Result = np.abs(coords[0]) + np.abs(coords[1])
    print(f"Day 12 part 1 solution: {part1Result}")
    timer.stop()

    # Part 2

    timer = ExecutionTimer()
    shipCoords = [0, 0]
    waypointCoords = [10, 1] # ALWAYS relative to ship
    for instruction in instructions:
        code, value = instruction[0], int(instruction[1:])
        if code in ["L", "R"]:
            waypointCoords = getRotatedWaypointPosition(waypointCoords, shipCoords, code, value)
        elif code == "F":
            shipCoords = moveShipTowardWaypoint(waypointCoords, shipCoords, value)
        elif code in ["N", "E", "S", "W"]:
            waypointCoords = getUpdatedPosition(waypointCoords, code, value)
        else:
            raise Exception("Invalid instruction")
    
    part2Result = np.abs(shipCoords[0]) + np.abs(shipCoords[1])
    print(f"Day 12 part 2 solution: {part2Result}")
    timer.stop()

if __name__ == "__main__":
    main()