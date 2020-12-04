from helpers import *

# Part 1

timer = executionTimer()
targetSum = 2020

numbers = getFileLines(1)

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
# apparently throwing an exception is genuinely the best way to break out of nested loops 🤦‍♂️
except Found:
    print('Day 1 part 1 solution: {0}'.format(n * o))
    timer.stopTimer()

# Part 2

timer = executionTimer()

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
    print('Day 1 part 2 solution: {0}'.format(n * o * p))
    timer.stopTimer()
