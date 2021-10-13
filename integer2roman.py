romans = {
    1000: "M", 
    900: "CM", 
    500: "D", 
    400: "CD", 
    100: "C", 
    90: "XC", 
    50: "L", 
    40: "XL", 
    10: "X", 
    9: "IX", 
    5: "V", 
    4: "IV", 
    1: "I"
    }


def roman(num):
    result = ""

    for key, value in romans.items():
        if num in romans:
            result += romans[num]
            return result

        mod = num//key

        if mod >= 1:
            result += mod*value
            num = num%key

    return result

def queryUser():
    while True:
        number = input("Type a number: ")

        if number == "":
            break
        
        else:
            print(roman(int(number)))

queryUser()