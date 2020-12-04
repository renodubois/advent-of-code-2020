from functools import reduce
from operator import mul

def openInput():
    with open('./input.txt', 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData

def calcSlope(slope, input):
    trees = 0
    nextX = 0
    nextY = 0
    while True:
        nextX += slope[0]
        nextY += slope[1]
        if nextY >= len(input):
            return trees
        nextRow = input[nextY]
        if nextX >= len(nextRow):
            nextX = nextX - len(nextRow)
        if nextRow[nextX] == '#':
            trees += 1


if __name__ == "__main__":
    # TODO: set day
    input = openInput()
    newInput = []
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]
    results = []
    for slope in slopes:
        totalSlopes = 1
        trees = calcSlope(slope, input)
        results.append(trees)
        totalSlopes = totalSlopes * trees
    print(reduce(mul, results))
