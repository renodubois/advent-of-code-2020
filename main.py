def openInput(day):
    with open('./{}/input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.splitlines()
        return splitData


def puzzle1(input):
    pass


def puzzle2(input):
    pass


if __name__ == "__main__":
    # TODO: set day
    day = "01"
    input = openInput(day)
    pass
