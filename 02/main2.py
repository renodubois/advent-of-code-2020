import re

def openInput(day, puzzle):
    with open('./{}/input{}.txt'.format(day, puzzle), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

def checkPassword(password):
    res = re.search(r'(\d{1,2})-(\d{1,2}) ([a-z]): ([a-z]+)', password)
    firstIndex, secondIndex, requiredChar, passToCheck = res.groups()
    firstIndex = int(firstIndex) - 1
    secondIndex = int(secondIndex) - 1
    firstCheck = passToCheck[firstIndex] == requiredChar
    secondCheck = passToCheck[secondIndex] == requiredChar
    return firstCheck ^ secondCheck    


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
