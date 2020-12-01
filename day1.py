import time

targetSum = 2020

with open('./inputs/1.txt') as file:
    numbers = [int(line.rstrip('\n')) for line in file]

evenNumbers = list(filter(lambda x: x%2 == 0, numbers))
oddNumbers = list(filter(lambda x: x%2 != 0, numbers))
numbersSuperList = [evenNumbers, oddNumbers]

class Found(Exception): pass

start = time.time()
try:
    for numberList in numbersSuperList:
        smallestValue = min(numberList)
        for n in numberList:
            if (n < targetSum - smallestValue):
                for o in numberList:
                    if (n + o == targetSum):
                        end = time.time()
                        raise Found
except Found:
    print('Day 1 part 1 solution: {0}'.format(n * o))
    print('Execution took {0} ms'.format((end - start) * 1000))