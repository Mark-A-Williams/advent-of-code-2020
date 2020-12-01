import time

# Part 1

start = time.time()
targetSum = 2020

with open('./inputs/1.txt') as file:
    numbers = [int(line.rstrip('\n')) for line in file]

evenNumbers = list(filter(lambda x: x%2 == 0, numbers))
oddNumbers = list(filter(lambda x: x%2 != 0, numbers))
numbersSuperList = [evenNumbers, oddNumbers]

class Found(Exception): pass

try:
    for numberList in numbersSuperList:
        smallestValue = min(numberList)
        for n in numberList:
            if (n < targetSum - smallestValue):
                for o in numberList:
                    if (n + o == targetSum):
                        raise Found
except Found:
    end = time.time()
    print('Day 1 part 1 solution: {0}'.format(n * o))
    print('Execution took {0} ms'.format((end - start) * 1000))

# Part 2

start = time.time()

try:
    for counter, numberList in enumerate(numbersSuperList):
        otherList = numbersSuperList[counter - 1]
        smallestValueInOtherList = min(otherList)
        for n in numberList:
            if (n < targetSum - 2 * smallestValueInOtherList):
                for o in otherList:
                    # the following check took execution for this part from 15-20 ms down to 1ms!
                    if (n + o < targetSum - smallestValueInOtherList):
                        for p in otherList: 
                            if (n + o + p == targetSum):
                                raise Found
except Found:
    end = time.time()
    print('Day 1 part 2 solution: {0}'.format(n * o * p))
    print('Execution took {0} ms'.format((end - start) * 1000))