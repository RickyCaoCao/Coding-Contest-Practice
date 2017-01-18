#-------------------------------------------------------------------------------
# Name:        ACSL 3
# Purpose:
#
# Author:      Richard Cao
#
# Created:     17-02-2015
# Copyright:   (c) Richard Cao 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def PossibleMoves(currentPos):
    quotient = (currentPos - 1) // 7
    remainder = (currentPos-1) % 7
    winMoveList = []
    leftMoveList = []
    rightMoveList = []
    upMoveList = []
    downMoveList = []
    topLeftMoveList = []
    topRightMoveList = []
    bottomLeftMoveList = []
    bottomRightMoveList = []

    #Horizontal
    #Left
    for i in range(6):
        left = 7 * quotient + remainder + 1 - (i + 1)
        if left in removedParts:
            break
        else:
            if left > 0:
                if ((left-1) // 7 == quotient):
                    leftMoveList.append(left)
    #right
    for i in range(6):
        right = 7 * quotient + remainder + 1 + (i+1)
        if right in removedParts:
            break
        else:
            if right < 50:
                if ((right-1) // 7 == quotient):
                    rightMoveList.append(right)

    #Vertical
    #Up
    for i in range(6):
        up = (quotient + i + 1) * 7 + remainder + 1
        if up in removedParts:
            break
        else:
            if up < 50:
                upMoveList.append(up)
    #Down
    for i in range(6):
        down = (quotient - i - 1) * 7 + remainder + 1
        if down in removedParts:
            break
        else:
            if down > 0:
                downMoveList.append(down)

    #Diagonal
    #TopLeft
    for i in range(6):
        topLeft = 7 * (quotient + (i+1)) + remainder + 1 - (i+1)
        if topLeft in removedParts:
            break
        else:
            if topLeft < 50:
                    if ((topLeft-1) // 7) == quotient + (i+1):
                        topLeftMoveList.append(topLeft)

    #TopRight
    for i in range(6):
        topRight = 7 * (quotient + (i+1)) + remainder + 1 + (i+1)
        if topRight in removedParts:
            break
        else:
            if topRight < 50:
                    if ((topRight-1) // 7) == quotient + (i+1):
                        topRightMoveList.append(topRight)

    #BottomLeft
    for i in range(6):
        bottomLeft = 7 * (quotient - (i+1)) + remainder + 1 - (i+1)
        if bottomLeft in removedParts:
            break
        else:
            if bottomLeft > 0:
                if ((bottomLeft-1) // 7) == quotient - (i+1):
                    bottomLeftMoveList.append(bottomLeft)

    #BottomRight
    for i in range(6):
        bottomRight = 7 * (quotient - (i+1)) + remainder + 1 + (i+1)
        if bottomRight in removedParts:
            break
        else:
            if bottomRight > 0:
                if ((bottomRight-1) // 7) == quotient - (i+1):
                    bottomRightMoveList.append(bottomRight)


    moveList = [leftMoveList, rightMoveList, upMoveList, downMoveList, topLeftMoveList, topRightMoveList, bottomLeftMoveList, bottomRightMoveList]
    for someList in moveList:
        for item in someList:
            if item in enemyMoves:
                winMoveList = someList

    if winMoveList == []:
        winMoveList = ["NONE"]


    return(winMoveList)

def SurroundingSquares(currentPos):
    quotient = (currentPos - 1) // 7
    remainder = (currentPos - 1) % 7
    moveList = []

    #Horizontal
    #Left
    left = 7 * quotient + (remainder + 1) - 1
    if left not in removedParts:
        if left > 0:
            if ((left-1) // 7 == quotient):
                moveList.append(left)
    #right
    right = 7 * quotient + (remainder + 1) + 1
    if right not in removedParts:
        if right < 50:
            if ((right-1) // 7 == quotient):
                moveList.append(right)

    #Vertical
    #Up
        up = (quotient + 1) * 7 + remainder + 1
        if up not in removedParts:
            if up < 50:
                moveList.append(up)
    #Down
    down = (quotient - 1) * 7 + remainder + 1
    if down not in removedParts:
        if down > 0:
            moveList.append(down)

    #Diagonal
    #TopLeft
    topLeft = 7 * (quotient + 1) + (remainder + 1) - 1
    if topLeft not in removedParts:
        if topLeft < 50:
                if ((topLeft-1) // 7) == quotient + 1:
                    moveList.append(topLeft)

    #TopRight
    topRight = 7 * (quotient + 1) + remainder + 1 + 1
    if topRight not in removedParts:
        if topRight < 50:
                if ((topRight-1) // 7) == quotient + 1:
                    moveList.append(topRight)

    #BottomLeft
    bottomLeft = 7 * (quotient - 1) + remainder + 1 - 1
    if bottomLeft not in removedParts:
        if bottomLeft > 0:
            if ((bottomLeft-1) // 7) == quotient - 1:
                moveList.append(bottomLeft)

    #BottomRight
    bottomRight = 7 * (quotient - 1) + remainder + 1 + 1
    if bottomRight not in removedParts:
        if bottomRight > 0:
            if ((bottomRight-1) // 7) == quotient - 1:
                moveList.append(bottomRight)
    return(moveList)


numberOfTimes = 0
while numberOfTimes < 5:
    numberOfTimes += 1

    someInput = input()
    aList = []
    aList = someInput.split(", ")

    inputList = []
    for item in aList:
        inputList.append(int(item))

    #need to remove space before int
    enemyCounter = inputList[0]
    friendlyCounter = inputList[1]
    removedParts = inputList[:-1]
    enemyMoves = []
    ourMoves = []
    enemyMoves = SurroundingSquares(enemyCounter)
    ourMoves = PossibleMoves(friendlyCounter)

    print(str(ourMoves)[1:-1])


