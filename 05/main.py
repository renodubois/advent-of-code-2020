import re

def openInput(day):
#    with open('./testinput.txt'.format(day), 'r') as file:
    with open('./input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData


def parseRow(input):
    lower = 0
    upper = 127
    i = 128
    for char in input:
        i = i / 2
        if char == 'F':
           upper -= i
        elif char == 'B':
            lower += i
    return lower


def parseCol(input):
    lower = 0
    upper = 7
    i = 8
    for char in input:
        i = i / 2
        if char == 'L':
            upper -= i
        elif char == 'R':
            lower += i
    return lower


def puzzle1(input):
    highestId = -1
    highestRow = -1
    highestCol = -1
    seats = {key: []  for key in range(0,120)}
    for line in input: 
        match = re.search(r'([FB]{7})([LR]{3})', line)
        row, col = match.groups()
        row = parseRow(row) 
        col = parseCol(col)
        seatId = (row * 8) + col
        seats[row].append(col)
        if row > highestRow:
            highestRow = row
        if col > highestCol:
            highestCol = col
        if seatId > highestId:
            highestId = seatId
            
    print(highestId)
    print(highestCol)
    print(highestRow)
    print(seats)


def puzzle2(input):
    highestId = -1
    highestRow = -1
    highestCol = -1
    seats = {key: []  for key in range(0,120)}
    for line in input: 
        match = re.search(r'([FB]{7})([LR]{3})', line)
        row, col = match.groups()
        row = parseRow(row) 
        col = parseCol(col)
        seatId = (row * 8) + col
        seats[row].append(col)
        if row > highestRow:
            highestRow = row
        if col > highestCol:
            highestCol = col
        if seatId > highestId:
            highestId = seatId
    seats = { key: value for key, value in seats.items() if len(value) > 0 }
    for row, seatsTaken in seats.items():
        if len(seatsTaken) < 8 and (row != 6 and row != 100):
            # NOTE: I did this manually, and I don't want to write this right now
            myRow = seatsTaken


if __name__ == "__main__":
    # TODO: set day
    day = "01"
    input = openInput(day)
    puzzle2(input)
    pass
