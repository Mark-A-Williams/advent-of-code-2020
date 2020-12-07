from __future__ import annotations
from helpers import * 

class Bag:
    def __init__(self, descriptor: str, containedBags: dict[str, int]):
        self.descriptor = descriptor
        self.containedBags = containedBags

    def containsBagWithDescriptor(self, topLevelBags: list[Bag], requiredDescriptor: str) -> bool:
        if requiredDescriptor in self.descriptor:
            return False
        if len(self.containedBags) == 0:
            return False
        if any(requiredDescriptor in bag for bag in self.containedBags.keys()):
            return True
        for containedBagDescriptor in self.containedBags.keys():
            topLevelBag = next(bag for bag in topLevelBags if bag.descriptor == containedBagDescriptor)
            if (topLevelBag.containsBagWithDescriptor(topLevelBags, requiredDescriptor)):
                return True
        return False

    def getBagsContainedInBag(self, topLevelBags: list[Bag]) -> int:
        raise("WIP")

def setUpBagFromLine(line: str) -> Bag:
    [descriptor, content] = line.split("bags contain")
    trimmedDescriptor = descriptor.strip()

    if "no other bags" in content:
        return Bag(trimmedDescriptor, {})

    subBagsDictionary: dict[str, int] = {}

    containedBags = [element.strip() for element in content.rstrip(".").replace("bags", "").replace("bag", "").split(",")]
    for bag in containedBags:
        subBagsDictionary[bag[2:]] = int(bag[0])

    return Bag(trimmedDescriptor, subBagsDictionary)

def main():
    allBags = [setUpBagFromLine(line) for line in getFileLines(7)]

    # Part 1

    timer = ExecutionTimer()
    count = 0
    for bag in allBags:
        if bag.containsBagWithDescriptor(allBags, "shiny gold"):
            count += 1
    print('Day 7 part 1 solution: {0}'.format(count))
    timer.stop()

if __name__ == "__main__":
    main()