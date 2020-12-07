from __future__ import annotations
from helpers import * 

class Bag:
    def __init__(self, descriptor: str, containedBags: list[str]):
        self.descriptor = descriptor
        self.containedBags = containedBags

    def containsBagWithDescriptor(self, topLevelBags: list[Bag], requiredDescriptor: str) -> bool:
        if requiredDescriptor in self.descriptor:
            return False
        if len(self.containedBags) == 0:
            return False
        if any(requiredDescriptor in bag for bag in self.containedBags):
            return True
        for containedBagDescriptor in self.containedBags:
            topLevelBag = next(bag for bag in topLevelBags if bag.descriptor == containedBagDescriptor)
            if (topLevelBag.containsBagWithDescriptor(topLevelBags, requiredDescriptor)):
                return True
        return False

def setUpBagFromLine(line: str) -> Bag:
    [descriptor, content] = line.split("bags contain")
    trimmedDescriptor = descriptor.strip()
    if "no other bags" in content:
        return Bag(trimmedDescriptor, [])
    containedBags = [bag.strip()[2:] for bag in content.rstrip(".").replace("bags", "").replace("bag", "").split(",")]
    return Bag(trimmedDescriptor, containedBags)

def main():
    timer = ExecutionTimer()
    allBags = [setUpBagFromLine(line) for line in getFileLines(7)]
    count = 0
    for bag in allBags:
        if bag.containsBagWithDescriptor(allBags, "shiny gold"):
            count += 1
    print('Day 7 part 2 solution: {0}'.format(count))
    timer.stop()

if __name__ == "__main__":
    main()