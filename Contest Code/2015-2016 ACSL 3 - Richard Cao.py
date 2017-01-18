#-------------------------------------------------------------------------------
# Project Title: ACSL #3
# Purpose: Definitely the hardest question I have done for ACSL
#
# Author:      Richard Cao
#
# Created:     05/03/2016
#
# As a WMCI Computer Science student, I state on my honour that I will:
# - cite any help that I have received (from other students, forums, etc.) on this assignment
# - not share actual program code with others. I realize that I am ENCOURAGED to discuss my approaches to solving problems, but that I should not share actual code.
# - be ready to explain any parts of the code I submit. I know that if I don't understand what something does, it doesn't belong in my assignment.
# -
# Inputs:
# - 9, 17, 22, 26, 4, A, 7, C, 18, C, 19, C, 32
# - 11, 16, 20, 27, 4, A, 7, B, 19, A, 24, B, 30
# - 9, 14, 23, 28, 3, B, 7, C, 25, A, 30
# - 8, 15, 23, 28, 4, A, 7, C, 24, C, 33, A, 30
# - 9, 16, 23, 26, 4, A, 7, B, 19, B, 25, B, 18
#-------------------------------------------------------------------------------
def InputFormat(theArray, returnInt):
    if returnInt == True:
        someNum = int(theArray[0])
        theArray.pop(0)
        return someNum
    elif returnInt == False:
        someLetter = theArray[0]
        theArray.pop(0)
        return someLetter

def MissingLetter(anArray):
    if "A" not in anArray:
        return ("A")
    elif "B" not in anArray:
        return("B")
    else:
        return("C")

letterArray = []
for i in range (36):
    letterArray.append(0)

inputArray = input().split(", ")

for i in range(4):
    aNum = InputFormat(inputArray, True)
    letterArray[aNum-1] = "X"

numOfLetters = InputFormat(inputArray, True)

for i in range(numOfLetters):
    aLetter = InputFormat(inputArray, False)
    aNum = InputFormat(inputArray, True)
    letterArray[aNum-1] = aLetter

#Row Checks
for i in range(4):
    leftSideNum = 6*i + 7
    rightSideNum = 6*i + 12
    if letterArray[leftSideNum-1] != 0:
        nextNumCheck = leftSideNum + 1
        while nextNumCheck != 0:
            if letterArray[nextNumCheck - 1] == 0 or letterArray[nextNumCheck-1] == letterArray[leftSideNum-1]:
                letterArray[nextNumCheck - 1] = letterArray[leftSideNum -1]
                nextNumCheck = 0
            else:
                nextNumCheck += 1
    if letterArray[rightSideNum-1] != 0:
        nextNumCheck = rightSideNum - 1
        while nextNumCheck != 0:
            if letterArray[nextNumCheck - 1] == 0 or letterArray[nextNumCheck-1] == letterArray[rightSideNum-1]:
                letterArray[nextNumCheck - 1] = letterArray[rightSideNum - 1]
                nextNumCheck = 0
            else:
                nextNumCheck -= 1

#Column Checks
for i in range(4):
    topSideNum = 2 + i
    bottomSideNum = 32 + i
    if letterArray[topSideNum-1] != 0:
        nextNumCheck = topSideNum + 6
        while nextNumCheck != 0:
            if letterArray[nextNumCheck - 1] == 0 or letterArray[nextNumCheck-1] == letterArray[topSideNum-1]:
                letterArray[nextNumCheck - 1] = letterArray[topSideNum -1]
                nextNumCheck = 0
            else:
                topSideNum += 6
    if letterArray[bottomSideNum-1] != 0:
        nextNumCheck = bottomSideNum - 6
        while nextNumCheck != 0:
            if letterArray[nextNumCheck - 1] == 0 or letterArray[nextNumCheck-1] == letterArray[bottomSideNum-1]:
                letterArray[nextNumCheck - 1] = letterArray[bottomSideNum - 1]
                nextNumCheck = 0
            else:
                nextNumCheck -= 6


finalArray = []
for factor in range(4):
    for addend in range(4):
        calcNum = 6 * factor + 8 + addend
        finalArray.append(letterArray[calcNum-1])


#Making Columns and Rows
column1 = []
column2 = []
column3 = []
column4 = []
row1 = []
row2 = []
row3 = []
row4 = []
emptyBoxArray = []


for i in range(4):
    row1.append(finalArray[i+0])
    row2.append(finalArray[i+4])
    row3.append(finalArray[i+8])
    row4.append(finalArray[i+12])
    column1.append(finalArray[4*i])
    column2.append(finalArray[4*i+1])
    column3.append(finalArray[4*i+2])
    column4.append(finalArray[4*i+3])

allRows = [row1, row2, row3, row4]
allColumns = [column1, column2, column3, column4]

emptyBoxArray.append(row1.count(0))
emptyBoxArray.append(row2.count(0))
emptyBoxArray.append(row3.count(0))
emptyBoxArray.append(row4.count(0))
emptyBoxArray.append(column1.count(0))
emptyBoxArray.append(column2.count(0))
emptyBoxArray.append(column3.count(0))
emptyBoxArray.append(column4.count(0))

#Two Algorithms to Solve the Puzzle
#First Algorithm
while emptyBoxArray.count(0) < 8:
    while 1 in emptyBoxArray:
        if emptyBoxArray.index(1) < 4:
            rowNum = emptyBoxArray.index(1) #from 0-3
            columnNum = allRows[rowNum].index(0) #from 0-3
            findLetter = MissingLetter(allRows[rowNum])

        elif emptyBoxArray.index(1) >= 4:
            columnNum = emptyBoxArray.index(1) - 4
            rowNum = allColumns[columnNum].index(0)
            findLetter = MissingLetter(allColumns[columnNum])

        finalArray[rowNum * 4 + columnNum] = findLetter
        #changing all the values
        allRows[rowNum][columnNum] = findLetter
        allColumns[columnNum][rowNum] = findLetter
        emptyBoxArray[rowNum] -= 1
        emptyBoxArray[columnNum+4] -= 1

    foundSolution = False
    i = 0
    while foundSolution == False and i < 8:
        if emptyBoxArray[i] == 2:
            foundSolution = False
            #rows
            if i < 4:
                rowNum = i
                temporaryArray = []
                for item in allRows[rowNum]:
                    temporaryArray.append(item)
                columnPosition1 = temporaryArray.index(0)
                temporaryArray.remove(0)
                columnPosition2 = temporaryArray.index(0) + 1

                if "A" not in allRows[rowNum]:
                    if "A" in allColumns[columnPosition1]:
                        #A is in the column position 2 then
                        columnNum = columnPosition2
                        specialLetter ="A"
                        foundSolution = True

                    elif "A" in allColumns[columnPosition2]:
                        columnNum = columnPosition1
                        specialLetter ="A"
                        foundSolution = True

                if "B" not in allRows[rowNum]:
                    if "B" in allColumns[columnPosition1]:
                        #B is in the column position 2 then
                        columnNum = columnPosition2
                        specialLetter ="B"
                        foundSolution = True

                    elif "B" in allColumns[columnPosition2]:
                        columnNum = columnPosition1
                        specialLetter ="B"
                        foundSolution = True

                if "C" not in allRows[rowNum]:
                    if "C" in allColumns[columnPosition1]:
                        #C is in the column position 2 then
                        columnNum = columnPosition2
                        specialLetter ="C"
                        foundSolution = True

                    elif "C" in allColumns[columnPosition2]:
                        columnNum = columnPosition1
                        specialLetter ="C"
                        foundSolution = True
            #columns
            elif i >= 4:
                columnNum = i - 4

                temporaryArray = []
                for item in allColumns[columnNum]:
                    temporaryArray.append(item)

                rowPosition1 = temporaryArray.index(0)
                temporaryArray.remove(0)
                rowPosition2 = temporaryArray.index(0) + 1

                if "A" not in allColumns[columnNum]:
                    if "A" in allRows[rowPosition1]:
                        #A is in the column position 2 then
                        rowNum = rowPosition2
                        specialLetter ="A"
                        foundSolution = True

                    elif "A" in allRows[rowPosition2]:
                        rowNum = rowPosition1
                        specialLetter ="A"
                        foundSolution = True

                if "B" not in allColumns[columnNum]:
                    if "B" in allRows[rowPosition1]:
                        #B is in the column position 2 then
                        rowNum = rowPosition2
                        specialLetter ="B"
                        foundSolution = True

                    elif "B" in allRows[rowPosition2]:
                        rowNum = rowPosition1
                        specialLetter ="B"
                        foundSolution = True

                if "C" not in allColumns[columnNum]:
                    if "C" in allRows[rowPosition1]:
                        #C is in the column position 2 then
                        rowNum = rowPosition2
                        specialLetter ="C"
                        foundSolution = True

                    elif "C" in allRows[rowPosition2]:
                        rowNum = rowPosition1
                        specialLetter ="C"
                        foundSolution = True

            if foundSolution == True:
                finalArray[rowNum * 4 + columnNum] = specialLetter
                #changing all the values
                allRows[rowNum][columnNum] = specialLetter
                allColumns[columnNum][rowNum] = specialLetter
                emptyBoxArray[rowNum] -= 1
                emptyBoxArray[columnNum+4] -= 1

        i += 1

while "X" in finalArray:
    finalArray.remove("X")

answerString = "".join(finalArray)
print(answerString)






