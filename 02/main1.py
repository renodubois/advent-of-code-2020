import re

def openInput(day, puzzle):
    with open('./{}/input{}.txt'.format(day, puzzle), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

def checkPassword(password):
    res = re.search(r'(\d{1,2})-(\d{1,2}) ([a-z]): ([a-z]+)', password)
    lowerBound, upperBound, requiredChar, passToCheck = res.groups()
    count = 0
    for char in passToCheck:
        if char == requiredChar:
            count += 1
            if count > int(upperBound):
                return False
    if count >= int(lowerBound) and count <= int(upperBound):
        return True
    return False


if __name__ == "__main__":
    # TODO: set day
    day = "02"
    puzzle = 1
    input = openInput(day, puzzle)
    validPasswords = 0
    for password in input:
        if checkPassword(password):
            validPasswords += 1
    print(validPasswords)
    exit()
