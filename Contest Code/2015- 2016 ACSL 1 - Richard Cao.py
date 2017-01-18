#-------------------------------------------------------------------------------
# Name:        2015-2016 ACSL #1
# Author:      Richard Cao
#-------------------------------------------------------------------------------
userinput = input()
userinput = userinput.split(', ')
printList = []
for i in range(0, len(userinput)-1):
    printList.append((bin(int(userinput[i+1]))[2:]))
    while len(printList[i]) < 3:
        printList[i] = "0" + printList[i]
printString = ' '.join(printList)

specialPermNum = int(userinput[0])
specialPermList = [0, 0, 0]
for i in range(0, len(specialPermList)):
    if specialPermNum == 2**i:
        specialPermList[i] = 1

permList = []
iterate = 0
for i in range(0, len(printList)):
    iterate += 1
    aterm = ['-', '-', '-']
    if printList[i][0] == '1':
        aterm[0] = 'r'
    if printList[i][1] == '1':
        aterm[1] = 'w'
    if printList[i][2] == '1':
        if specialPermList[i] == 1:
            if i == len(printList) - 1:
                aterm[2] = 't'
            else:
                aterm[2] = 's'
        else:
            aterm[2] = 'x'
    newTerm = ''.join(aterm)
    permList.append(newTerm)

permListString = ' '.join(permList)

print(printString, "and", permListString)