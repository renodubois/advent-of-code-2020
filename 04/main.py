import re

def openInput(day):
    with open('input.txt'.format(day), 'r') as file:
        data = file.read()
        splitData = data.split('\n\n')
        formattedSplitData = []
        for line in splitData:
            formattedSplitData.append(line.replace('\n', ' '))
        return formattedSplitData


def validateFields(data):
    eyeColors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    for key, value in data.items():
        if key in ['byr', 'iyr', 'eyr']:
            if len(value) != 4:
                return False
            year = int(value)
            if key == 'byr':
                if year < 1920 or year > 2002:
                    return False
            elif key == 'iyr':
                if year < 2010 or year > 2020:
                    return False
            elif key == 'eyr':
                if year < 2020 or year > 2030:
                    return False
        elif key == 'hgt':
            res = re.search(r'(\d{2,3})(in|cm)', value.lower())
            if not res:
                return False
            height, unit = res.groups()
            height = int(height)
            if (unit == 'cm' and (height < 150 or height > 193)) or (unit == 'in' and (height < 59 or height > 76)):
                return False
        elif key == 'hcl':
            res = re.search(r'#[a-z0-9]{6}', value.lower())
            if not res:
                return False
        elif key == 'ecl':
            if not value in eyeColors:
                return False
        elif key == 'pid':
            if len(value) != 9:
                return False
    return True

def puzzle1(input):
    validPassports = 0
    requiredFields = 'byr,ecl,eyr,hcl,hgt,iyr,pid'
    for line in input:
        newLine = line.split(' ')
        newLine = [x.split(':')[0] for x in newLine]
        newLine.sort()
        newLine = [x for x in newLine if x != 'cid']
        lineString = ','.join(newLine)
        if lineString == requiredFields:
            validPassports += 1
    print(validPassports)

def puzzle2(input):
    validPassports = 0
    requiredFields = 'byr,ecl,eyr,hcl,hgt,iyr,pid'
    for line in input:
        newLine = line.split(' ')
        newLine = [x.split(':')[0] for x in newLine]
        newLine.sort()
        newLine = [x for x in newLine if x != 'cid']
        lineString = ','.join(newLine)
        if lineString == requiredFields:
            fieldData = dict([tuple(x.split(':')) for x in line.split(' ')])
            if validateFields(fieldData):
                validPassports += 1
    print(validPassports)

if __name__ == "__main__":
    # TODO: set day
    day = "04"
    input = openInput(day)
    puzzle2(input)
    pass
