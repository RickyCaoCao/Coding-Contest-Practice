#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Richard Cao
#
# Created:     17-02-2015
# Copyright:   (c) Richard Cao 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def CheckingPartners():
    classroomSize = int(input("Size of class."))
    classStringA = input("Second line")
    classStringB = input("Third line")
    ListA = classStringA.split()
    ListB = classStringB.split()
    judgement = "good"
    for person in ListA:
        placeInA = ListA.index(person)
        placeInB = ListB.index(person)
        if ListA[placeInB] != ListB[placeInA]:
            judgement = "bad"
        elif placeInA == placeInB:
            judgement = "bad"
    return judgement

print(CheckingPartners())

