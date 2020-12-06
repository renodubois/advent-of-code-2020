def openInput(day):
    with open('input.txt'.format(day), 'r') as file:
        return file.read()


def uniqueList(line):
    returnList = []
    for char in line:
        if not char in returnList:
            returnList.append(char)
    return returnList


def puzzle1(input):
    # separate on double newlines, for each group
    groups = input.split('\n\n')
    val = 0
    for group in groups:
        # list of individual characters
        formattedGroup = list(group.replace('\n', ''))
        val += len(uniqueList(formattedGroup))
    print(val)
    pass


def puzzle2(input):
    groups = input.split('\n\n')
    val = 0
    for group in groups:
        count = {}
        # get the number of lines in the group
        groupLength = len(group.split('\n'))
        formattedGroup = list(group.replace('\n', ''))
        for char in formattedGroup:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        validAnswers = [ x for (x, y) in count.items() if y == groupLength ]
        val += len(validAnswers)
    print(val)
    return


if __name__ == "__main__":
    # TODO: set day
    day = "01"
    input = openInput(day)
    #puzzle1(input)
    puzzle2(input)
