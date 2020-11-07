cardNumber = int(input("Enter your credit card number without spaces: "))

def isValid(number):
    number = str(number)
    cardIsValid = False

    result = sumDoubleEvenLocation(number) + sumOddLocation(number)

    prefix = isPrefix(number, "4") or isPrefix(number, "5") or  isPrefix(number, "6") or isPrefix(number, "37") 


    # getDigit(number) 
    # getPrefix(number, k)

    if (len(number) >= 13 and len(number) <=16) and (result%10 == 0) and prefix == True:
        cardIsValid = True
    
    return cardIsValid

def sumDoubleEvenLocation(number):
    temp = []
    count = 0
    count1 = 0

    for i in number[::2]:
        temp.append(i)

    temp = [int(a) for a in temp]

    while count < len(temp):
        temp[count] = temp[count]*2
        count += 1

    temp = [str(a) for a in temp]

    while count1 < len(temp):
        if len(temp[count1]) == 2:
            temp[count1] = sum([int(x) for x in temp[count1]])
        count1 += 1


    return sum([int(x) for x in temp])

# def getDigit(number):

def sumOddLocation(number):
    addition = 0

    for i in number[::-2]:
        addition += int(i)

    return addition

def isPrefix(number, d):
    prefix = False

    if getSize(d) == 1 and (number[0] == "4" or number[0] == "5" or number[0] == "6"):
        prefix = True

    elif getSize(d) == 2 and (number[0] == "3" and number[1] =="7"):
        prefix = True
    
    return prefix

def getSize(d):
    return len(str(d))

def getPrefix(number, k):
    newNumber = ""

    i = 0   
    
    if len(number) < k:
        newNumber = number

    else:
        while i < k:
            newNumber += (number[i])
            i += 1

    return newNumber


print(isValid(cardNumber))