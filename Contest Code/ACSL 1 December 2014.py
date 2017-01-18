#-------------------------------------------------------------------------------
# Name:        ACSL 1
# Purpose:
#
# Author:      Richard Cao (WMCI)
#
# Created:     13-12-2014
# Copyright:   (c) Richard Cao 2014
# Licence:     CC
#-------------------------------------------------------------------------------
#Time Functions
def TimeFunc(numTime, hourPart):
    if numTime == 12:
        numTime = 0
    if hourPart == "PM":
        numTime += 12
    return (numTime)

def TimeDifference (timeOne, timeTwo):
    if timeTwo - timeOne > 0:
        if timeTwo - timeOne <= 12:
            timeDifference = timeTwo - timeOne
            firstPersonEarly = True
        else:
            timeDifference = 24 - (timeTwo - timeOne)
            firstPersonEarly = False
    else:
        if timeOne - timeTwo <= 12:
            timeDifference = timeOne - timeTwo
            firstPersonEarly = False
        else:
            timeDifference = 24 - (timeOne - timeTwo)
            firstPersonEarly = True
    return(timeDifference, firstPersonEarly)

def timeTravelled(timeDifference, firstPersonWentFirst, firstSpeed, secondSpeed, totalDistance):
    if firstPersonWentFirst == True:
        someDistanceTravelled = firstSpeed * timeDifference
    else:
        someDistanceTravelled = secondSpeed * timeDifference
    leftoverDistance = totalDistance - someDistanceTravelled
    timeRequired = leftoverDistance/(firstSpeed + secondSpeed)
    if firstPersonWentFirst == True:
        totalTime = timeDifference + timeRequired
    else:
        totalTime = timeRequired
    return totalTime

#Calculating Function
def endTime(totalTime):
    timeInMinutes = totalTime * 60
    hours = int(round(timeInMinutes//60))
    minutes = int(round(timeInMinutes % 60))
    if (minutes/10) < 1:
        minutes = str("0" + str(minutes))
    if hours > 12:
        hours -= 12
    return(str(hours) + ":" + str(minutes))

#Distance Functions
def ChangeDef(desNum):
    if desNum == "A":
        desNum = 1
    elif desNum == "B":
        desNum = 2
    elif desNum == "C":
        desNum = 3
    elif desNum == "D":
        desNum = 4
    elif desNum == "E":
        desNum = 5
    elif desNum == "F":
        desNum = 6
    elif desNum == "G":
        desNum = 7
    elif desNum == "H":
        desNum = 8
    elif desNum == "J":
        desNum = 9
    elif desNum == "K":
        desNum = 10
    return desNum

def DistanceFunc(desOne, desTwo):
    desOne = ChangeDef(desOne)
    desTwo = ChangeDef(desTwo)
    desLengthsList = (450, 140, 125, 365, 250, 160, 380, 235, 320)
    actualDesList = desLengthsList[desOne-1:desTwo-1]
    totalLength = 0
    for i in actualDesList:
        totalLength += i
    return totalLength


#Actual Code
testNumber = 0
while testNumber != 5:
    originalString = input("Sample Input: 1. A, C, 1, PM, 2, PM, 50, 60")

    edittedString = originalString.replace(" ","")
    edittedString = edittedString.replace(".",",")
    edittedString = edittedString.split(",")

    print (edittedString)
    testNumber = edittedString[0]
    desOne = edittedString[1]
    desTwo = edittedString[2]
    numTimeOne = float(edittedString[3])
    hourPartOne = edittedString[4]
    numTimeTwo = float(edittedString[5])
    hourPartTwo = edittedString[6]
    speedOne = float(edittedString[7])
    speedTwo = float(edittedString[8])

    totalDistance = DistanceFunc(desOne, desTwo)

    calcTimeOne = TimeFunc(numTimeOne, hourPartOne)
    calcTimeTwo = TimeFunc(numTimeTwo, hourPartTwo)
    (differenceInTime, firstPersonWentFirst) = TimeDifference(calcTimeOne, calcTimeTwo)

    timeForTravel = timeTravelled(differenceInTime, firstPersonWentFirst, speedOne, speedTwo, totalDistance)
    print (endTime(timeForTravel))


