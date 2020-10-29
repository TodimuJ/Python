def main():
    inputNumber = input("Enter a string of digits to process or 'quit' to stop: ")

    while inputNumber != "quit":
        processStr(inputNumber)
        getHasRepeatDigit(inputNumber)
        inputNumber = input("\nEnter a string of digits to process or 'quit' to stop: ")


def processStr(inputNumber):
    addition = 0
    product = 1

    for number in inputNumber:
        addition = addition + int(number)
    
    for letter in inputNumber:
        product = product * int(letter)


    print("The sum of the digits in", inputNumber, "is", addition)
    print("The product of the digits in", inputNumber, "is", product)


def getHighest(inputNumber):
    temp = []

    for letter in inputNumber:
        temp.append(letter)

    #print("The highest digit in the given string is:", max(temp))

    return max(temp)


def getHasRepeatDigit(inputNumber):
    maximum = getHighest(inputNumber)

    temp = []

    for letter in inputNumber:
        temp.append(letter)

    temp.sort()

    isRepeat = False

    for i in range(0, len(temp)):
        for j in range(i + 1, len(temp)):
            if (temp[i] == temp[j]):
                isRepeat = True


    if isRepeat == True:
        print("The string has repeated digits")

    else:
        print("The string has no repeated digits")
        print("The highest digit in the given string is:", maximum)
                

main()