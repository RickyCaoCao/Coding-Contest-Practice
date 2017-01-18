#-------------------------------------------------------------------------------
# Name:        ACSL #4
# Purpose:
#
# Author:      Richard Cao
#
# Created:     09-04-2016
# Copyright:   (c) Richard Cao 2016
# Licence:     <your licence>
# Input: #, aac, acc, abc, ac, abbc, abbbc, abbbbc, aabc, aabbc
# Other Inputs: a.c, a[ab]c, a[^ab]c, ab*c, a.b{2,4}c
#-------------------------------------------------------------------------------

characterStrings = input().split(", ")
##someInput = '#, aac, acc, abc, ac, abbc, abbbc, abbbbc, aabc, aabbc'
##characterStrings = someInput.split(", ")
if '#' in characterStrings:
    characterStrings.remove('#')
    characterStrings.append('')

maxLength = 0
for item in characterStrings:
    length = len(item)
    if length > maxLength:
        maxLength = length

availableChars = []
lineOfStr = ''.join(characterStrings)
for i in range (len(lineOfStr)):
    char = lineOfStr[i]
    if char not in availableChars:
        availableChars.append(char)

##availableChars = ['a', 'c', 'b']
##newStr = "a[^ab]c"
##testing = [newStr]
##characterStrings = ['#', 'aac', 'acc', 'abc', 'ac', 'abbc', 'abbbc', 'abbbbc', 'aabc', 'aabbc']

def AnyFunction(someStr, testingCase):
    tempArray = []
    for item in testingCase:
        spot = item.index('.')
        for i in range(len(availableChars)):
            testString = item[:spot] + availableChars[i] + item[spot+1:]
            tempArray.append(testString)
    testingCase = tempArray[:]
    return(testingCase)

def LimitedRepeatFunction(someStr, testingCase):
    letter = someStr[iter-1]
    m = someStr[iter+1]
    n = someStr[iter+3]
##    letter = 'b'
##    m = '2'
##    n = '4'
    tempArray = []
    for item in testingCase:
        spot = item.index('{')
        for i in range (int(m), int(n)+1):
            addedStr = letter * i
            testString = item[:spot-1] + addedStr + item[spot+5:]
            tempArray.append(testString)
    testingCase = tempArray[:]
    return(testingCase)

##maxLength = 6
def FreeRepeatFunction(someStr, testingCase):
    letter = someStr[iter-1]
##    letter = 'b'
    tempArray = []
    for item in testingCase:
        length = len(item) - 2
        spot = item.index('*')
        for i in range(maxLength - length + 8):
            addStr = letter * i
            testString = item[:spot-1] + addStr + item[spot+1:]
            tempArray.append(testString)
    testingCase = tempArray[:]
    return(testingCase)

def PickCharFunction(someStr, testingCase):
##    i = 1
    exampleL = testingCase[0].index('[')
    exampleR = testingCase[0].index(']')
    charStr = testingCase[0][exampleL+1:exampleR]
    charArray = list(charStr)
    tempArray = []
    for item in testingCase:
        spotL = item.index('[')
        spotR = item.index(']')
        for letter in charArray:
            testString = item[:spotL] + letter + item[spotR+1:]
            tempArray.append(testString)
    testingCase = tempArray[:]
    return(testingCase)

def NotPickCharFunction(someStr, testingCase):
##    i = 1
    exampleL = testingCase[0].index('[')
    exampleR = testingCase[0].index(']')
    charStr = testingCase[0][exampleL+2:exampleR]
    charArray = list(charStr)
    tempArray = []
    for item in testingCase:
        spotL = item.index('[')
        spotR = item.index(']')
        for letter in availableChars:
            if letter not in charArray:
                testString = item[:spotL] + letter + item[spotR+1:]
                tempArray.append(testString)
    testingCase = tempArray[:]
    return(testingCase)

#Program
for i in range(5):
    oper = 0
    iter = 0
    check = 0
    newStr = input()
    testing = [newStr]
    while iter < len(newStr) and oper < 2:
        char = newStr[iter]
        if char == ".":
            testing = AnyFunction(newStr, testing)
            oper += 1
        elif char == '{':
            testing = LimitedRepeatFunction(newStr, testing)
            oper += 1
        elif char == '*':
            testing = FreeRepeatFunction(newStr, testing)
            oper += 1
        elif char == '[':
            if newStr[iter+1] == '^':
                testing = NotPickCharFunction(newStr, testing)
                oper += 1
            else:
                testing = PickCharFunction(newStr, testing)
                oper += 1
        iter += 1

    #Answer Converter
    finalArray = []

    for item in testing:
        if item in characterStrings:
            finalArray.append(item)

    if len(finalArray) != 0:
        answer = ', '.join(finalArray)
    else:
        answer = "NONE"

    print(answer)
