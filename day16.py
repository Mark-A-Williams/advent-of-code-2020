from helpers import *
from typing import List
from operator import add

def main():
    #test = "class: 1-3 or 5-7\nrow: 6-11 or 33-44\nseat: 13-40 or 45-50\n\nyour ticket:\n7,1,14\n\nnearby tickets:\n7,3,47\n40,4,50\n55,2,20\n38,6,12"

    with open('./inputs/16.txt') as file:
        groups = [group.split("\n") for group in file.read().split("\n\n")]

    # Part 1

    timer = ExecutionTimer()
    
    allowableRangesPerField = [criteria.replace(" or ", ",").split(": ")[1].split(",") for criteria in groups[0]]
    allAllowableRanges = [x.split("-") for x in sum(allowableRangesPerField, [])]
    
    bannedNumbers = [
        i for i in range(1000)
        if not any(int(range[0]) <= i and int(range[1]) >= i
        for range in allAllowableRanges)
    ]

    nearbyTickets = [ticket.split(",") for ticket in groups[2][1:]]
    invalidFields: List[int] = []

    for ticket in nearbyTickets:
        for field in ticket:
            if int(field) in bannedNumbers:
                invalidFields.append(int(field))

    part1Result = sum(invalidFields)
    print('Day 16 part 1 solution: {0}'.format(part1Result))
    timer.stop()

if __name__ == "__main__":
    main()