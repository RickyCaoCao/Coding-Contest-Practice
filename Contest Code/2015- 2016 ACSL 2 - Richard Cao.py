#-------------------------------------------------------------------------------
# Name:        2015-2016 ACSL #2
# Author:      Richard Cao
#-------------------------------------------------------------------------------

def STR(someFloat, someLength, someDecimal):
    theFloat = str(someFloat)
    length = int(someLength)
    decimal = int(someDecimal)

    numberPart = theFloat.split('.')[0]
    decimalPart = theFloat.split('.')[1]
    numberPartLength = len(numberPart)
    decimalPartLength = len(decimalPart)
    output = ''

##    print(numberPart)
##    print(decimalPart)
##    print(numberPartLength)
##    print(decimalPartLength)

    if length != 0:
        if decimal == 0:
            checkLength = length-(decimal + numberPartLength)
            if checkLength < 0:
                for i in range(length):
                    output += '#'
                return output
        else:
            checkLength = length-(decimal + 1 + numberPartLength)

        if checkLength < 0:
            for i in range (length-decimal-1):
                output += '#'
            output += '.'
            for i in range (decimal):
                output += '#'
        else:
            hashString = ''
            if decimal == 0:
                if checkLength > 0:
                    for i in range (checkLength):
                        hashString += '#'
                output = hashString + numberPart
                return output

            elif(decimal != decimalPartLength):
                if int(decimalPart[decimal]) < 5:
                    decimalPart = decimalPart[:decimal]
                elif int(decimalPart[decimal]) >= 5:
                    decimalPart = decimalPart[:decimal]
                    decimalPart = str(int(decimalPart)+1)
                if checkLength > 0:
                    for i in range (checkLength):
                        hashString += '#'
            output = hashString + numberPart + '.' + decimalPart
    return output

theInput = input()
inputFloat = theInput.split(', ')[0]
inputLength = theInput.split(', ')[1]
inputDecimal = theInput.split(', ')[2]

print(STR(inputFloat, inputLength, inputDecimal))