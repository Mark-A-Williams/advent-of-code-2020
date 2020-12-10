from helpers import *

def main():
    joltages = [int(line) for line in getFileLines(10)]

    # Part 1

    timer = ExecutionTimer()
    joltages.sort()

    numberOf1JoltGaps = numberOf3JoltGaps = 0
    for (counter, joltage) in enumerate(joltages):
        if counter == 0:
            if joltage == 1:
                numberOf1JoltGaps += 1
            elif joltage == 3:
                numberOf3JoltGaps += 1
        else:
            gapToNext = joltage - joltages[counter - 1]
            if gapToNext == 1:
                numberOf1JoltGaps += 1
            elif gapToNext == 3:
                numberOf3JoltGaps += 1

    result = numberOf1JoltGaps * (numberOf3JoltGaps + 1) # +1 for device adaptor
    print(f"Day 10 part 1 solution: {result}")
    timer.stop()

if __name__ == "__main__":
    main()