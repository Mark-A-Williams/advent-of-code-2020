from helpers import *

def main():
    with open('./inputs/6.txt') as file:
        groups: list[str] = [block.replace("\n", "") for block in file.read().split('\n\n')]

    # Part 1

    timer = ExecutionTimer()
    part1Solution = 0
    
    for group in groups:
        uniqueCharacters: list[str] = []
        for char in group:
            if not (char in uniqueCharacters):
                uniqueCharacters.append(char)
        part1Solution += len(uniqueCharacters)

    print('Day 6 part 1 solution: {0}'.format(part1Solution))
    timer.stop()

if __name__ == "__main__":
    main()