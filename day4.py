from helpers import ExecutionTimer
import re
from typing import List

def getPassportDictionary() -> List[dict[str, str]]:
    with open('./inputs/4.txt') as file:
        splitByLineBreaks = file.read().split('\n\n')
        return [mapToDict(block) for block in splitByLineBreaks]

def mapToDict(block: str) -> dict[str, str]:
    standardisedFormatBlocks = block.replace(' ', '\n').split('\n')
    return dict(block.split(':') for block in standardisedFormatBlocks)

def main():
    passports = getPassportDictionary()

    # Part 1
    timer = ExecutionTimer()
    requiredFields = [
        "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
    ]

    validPassports1: List[dict[str, str]] = []
    for passport in passports:
        if all(field in passport for field in requiredFields):
            validPassports1.append(passport)

    print('Day 4 part 1 solution: {0}'.format(len(validPassports1)))
    timer.stop()

    # Part 2
    timer = ExecutionTimer()
    validEyeColours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    validPassports2: List[dict[str, str]] = []
    for passport in validPassports1:
        if (re.match(r'^[0-9]{9}$', passport['pid']) and
            re.match(r'^#[0-9a-f]{6}$', passport['hcl']) and
            int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002 and
            int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020 and
            int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030 and
            passport['ecl'] in validEyeColours):
                hgt = passport['hgt']
                unit = hgt[-2:]
                try:
                    number = int(hgt[:len(hgt)-2])
                    if ((unit == "in" and number >= 59 and number <= 76) or
                        unit == "cm" and number >= 150 and number <= 193):
                        validPassports2.append(passport)
                except ValueError:
                    # If the number's not valid, the passport sure as hell ain't 🧠
                    pass

    print('Day 4 part 2 solution: {0}'.format(len(validPassports2)))
    timer.stop()

if (__name__ == '__main__'):
    main()
