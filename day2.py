from helpers import executionTimer

timer = executionTimer()

class PasswordWithPolicy:
    def __init__(
        self,
        password: str,
        requiredCharacter: str,
        firstInt: int,
        secondInt: int):
        self.password = password
        self.requiredCharacter = requiredCharacter
        self.firstInt = firstInt
        self.secondInt = secondInt

    def isValid(self) -> bool:
        return (self.password.count(self.requiredCharacter) >= self.firstInt
            and self.password.count(self.requiredCharacter) <= self.secondInt)

    def isValidUnderOfficialTobogganCorporatePolicy(self) -> bool:
        isInFirstPosition = (len(self.password) > self.firstInt - 1
                            and self.password[self.firstInt - 1] == self.requiredCharacter)
        isInSecondPosition = (len(self.password) > self.secondInt - 1
                            and self.password[self.secondInt - 1] == self.requiredCharacter)
        return isInFirstPosition != isInSecondPosition

def parsePassword(rawPassword: str) -> PasswordWithPolicy:
    strippedPassword = rawPassword.replace(':','')
    [counts, character, password] = strippedPassword.split(' ')
    [minCount, maxCount] = [int(count) for count in counts.split('-')]
    return PasswordWithPolicy(password, character, minCount, maxCount)

# Part 1

with open('./inputs/2.txt') as file:
    passwordsAndPolicies = [parsePassword(line.rstrip('\n')) for line in file]

validPasswordsCount = 0
for passwordAndPolicy in passwordsAndPolicies:
    if passwordAndPolicy.isValid(): validPasswordsCount += 1

print('Day 2 part 1 solution: {0}'.format(validPasswordsCount))
timer.stopTimer()

# Part 2

timer = executionTimer()

validPasswordsCount = 0
for passwordAndPolicy in passwordsAndPolicies:
    if passwordAndPolicy.isValidUnderOfficialTobogganCorporatePolicy(): validPasswordsCount += 1
        
print('Day 2 part 2 solution: {0}'.format(validPasswordsCount))
timer.stopTimer()
