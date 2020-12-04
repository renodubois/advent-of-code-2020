def openInput():
    with open('./input.txt', 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData


if __name__ == "__main__":
    # TODO: set day
    input = openInput()
    newInput = []
    trees = 0
    nextX = 0
    nextY = 0
    while True:
        nextX += 3
        nextY += 1
        if nextY >= len(input):
            print(trees)
            exit()
        nextRow = input[nextY]
        if nextX >= len(nextRow):
            nextX = nextX - len(nextRow)
        if nextRow[nextX] == '#':
            trees += 1
    pass
