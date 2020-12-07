from __future__ import annotations
from helpers import *

class Bag:
    def __init__(self, descriptor: str):
        self.descriptor = descriptor
        self.containedBags: list[str] = []

    def containsBagWithDescriptor(self, topLevelBags: list[Bag], descriptor: str) -> bool:
        if len(self.containedBags) == 0:
            return False
        if any(bag.descriptor == descriptor for bag in self.containedBags):
            return True
        for referencedBag in self.containedBags:
            topLevelBag = next((bag for bag in topLevelBags if bag.descriptor == referencedBag), "none")
            if (topLevelBag != "none" and topLevelBag.containsBagWithDescriptor()):
                return True


def setUpBagFromLine(str: rawLine) -> Bag:
    # TODO
    return Bag()

def main():
    lines = getFileLines(7)
    for line in lines:
        [descriptor, content] = line.split(" contain ")
        if ("gold bag" in content):
            print(descriptor.rstrip("bags"))

if __name__ == "__main__":
    main()