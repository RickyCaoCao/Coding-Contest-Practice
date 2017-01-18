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

numberOfParticipants = int(input("Participants."))
numberOfRounds = int(input("Rounds"))
currentNumberOfRounds = 0
listOfParticipants = []
for i in range(numberOfParticipants):
    listOfParticipants.append(i+1)
while currentNumberOfRounds < numberOfRounds:
    currentNumberOfRounds += 1
    removalFactor = int(input("Removal Factor"))
    a = 0
    removalList = []
    while (a + removalFactor) <= len(listOfParticipants):
        a += removalFactor
        removalList.append(listOfParticipants[a-1])
    for i in removalList:
        if i in listOfParticipants:
            listOfParticipants.remove(i)
for i in listOfParticipants:
    print(i)



