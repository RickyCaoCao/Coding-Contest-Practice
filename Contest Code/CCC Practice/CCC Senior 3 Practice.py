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
    factorOfSeven = currentPos // 7
    moveList = []
    for i in range(7):
        moveList.append(7*factorOfSeven + i + 1)
    print(moveList)


numberOfTimes = 0
while numberOfTimes < 5:
    numberOfTimes += 1

    someInput = "46, 4, 45, 47, 38, 40, 0"
    #someInput = input()
    inputList = []
    inputList = someInput.split(",")

    #need to remove space before int
    print(inputList)
    enemyCounter = inputList[0]
    friendlyCounter = inputList[1]
    removedParts = inputList[2:-1]
    enemyMoves = []
    ourMoves = []
    PossibleMoves(46);


