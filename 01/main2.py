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
    for i in range(0, len(input) - 2):
        a = int(input[i])
        for j in range(i+1, len(input)):
            b = int(input[j])
            for k in range (j+1, len(input)):
                c = int(input[k])
                sum = a + b + c
                if sum == 2020:
                    print(a * b * c)
                    exit()
    pass
