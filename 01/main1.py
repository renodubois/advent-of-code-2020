def openInput(day, puzzle):
    with open('./{}/input{}.txt'.format(day, puzzle), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData


if __name__ == "__main__":
    # TODO: set day
    day = "01"
    puzzle = 1
    input = openInput(day, puzzle)
    for i in range(0, len(input)):
        curNumber = int(input[i])
        for j in range(i+1, len(input)):
            otherNum = int(input[j])
            if (curNumber + otherNum) == 2020:
                print(curNumber * otherNum)
    pass
