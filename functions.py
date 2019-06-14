ones = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["ten", "twenty", "thrity", "forty", "fifty", "sixty", "seventy", "eight", "ninty"]
hundred = "hundred"


def input_ok(input):
    if input >=100:
        return False
    elif input <=0:
        return False
    else:
        return True

def convert_to_text(number):
    string = str(number)
    number_length = len(string)
    if number_length == 1:
        print(ones[number-1])
    
    elif number_length == 2:
        low_digit = int(string[1])
        mid_digit = int(string[0])
        if mid_digit == 1:
            print(teens[low_digit-1])
        else:
            x = tens[mid_digit-1] + " " + ones[low_digit-1]
            print(x)
    
    elif number_length == 3:
        low_digit = int(string[2])
        mid_digit = int(string[1])
        high_digit = int(string[0])
        if mid_digit == 1:
            b = teens[low_digit-1]
        else:
            b = tens[mid_dgit-1] + " " + ones[low_digit-1]
        print(ones[high_digit] + " " + hundred + " " + b)
    
    else:
        print("Error: bad input not caught")


