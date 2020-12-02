import re
import time

start = time.time()

class PasswordWithPolicy:
    def __init__(
        self,
        password: str,
        requiredCharacter: str,
        minCharacterCount: int,
        maxCharacterCount: int):
        self.password = password
        self.requiredCharacter = requiredCharacter
        self.minCharacterCount = minCharacterCount
        self.maxCharacterCount = maxCharacterCount

    def isValid(self) -> bool:
        return (self.password.count(self.requiredCharacter) >= self.minCharacterCount
            and self.password.count(self.requiredCharacter) <= self.maxCharacterCount)

def parsePassword(rawPassword: str):
    strippedPassword = rawPassword.replace(':','')
    [counts, character, password] = strippedPassword.split(' ')
    [minCount, maxCount] = [int(count) for count in counts.split('-')]
    return PasswordWithPolicy(password, character, minCount, maxCount)

with open('./inputs/2.txt') as file:
    passwordsAndPolicies = [parsePassword(line.rstrip('\n')) for line in file]

validPasswordsCount = 0
for passwordAndPolicy in passwordsAndPolicies:
    if passwordAndPolicy.isValid(): validPasswordsCount += 1

end = time.time()
print('Day 2 part 1 solution: {0}'.format(validPasswordsCount))
print('Execution took {0} ms'.format((end - start) * 1000))