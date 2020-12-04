from executionTimer import executionTimer
import re

def getPassportDictionary() -> list:
    with open('./inputs/4.txt') as file:
        splitByLineBreaks = file.read().split('\n\n')
        return [mapToDict(block) for block in splitByLineBreaks]

def mapToDict(block: str) -> list:
    standardisedFormatBlocks = block.replace(' ', '\n').split('\n')
    return dict(block.split(':') for block in standardisedFormatBlocks)

def main():
    passports = getPassportDictionary()

    # Part 1
    timer = executionTimer()
    requiredFields = [
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    ]

    validPassports = 0
    for passport in passports:
        if all(field in passport for field in requiredFields):
            validPassports += 1

    print('Day 4 part 1 solution: {0}'.format(validPassports))
    timer.stopTimer()

    # Part 2
    timer = executionTimer()
    validPassports = 0

    for passport in passports:
        if all(field in passport for field in requiredFields):
            if (re.match(r'[0-9]{9}', passport['pid'])):
                if (re.match(r'#[0-9a-f]{6}', passport['hcl'])):
                    # TODO byr, iyr, eyr, hgt, ecl
                    validPassports += 1

    print('Day 4 part 2 solution: {0}'.format(validPassports))
    timer.stopTimer()


if (__name__ == '__main__'):
    main()
