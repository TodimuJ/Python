def binarySearch(array, number):
    bIndex = 0
    eIndex = len(array) - 1 

    while bIndex <= eIndex:
        midpoint = bIndex + (eIndex - bIndex) // 2
        midpoint_value = array[midpoint]

        if midpoint_value == number:
            return midpoint
        
        elif number < midpoint_value:
            eIndex = midpoint - 1
        
        elif number > midpoint_value:
            bIndex = midpoint + 1

    return None

sequence = [2, 4, 1, 7, 8, 3, 96, 340, 76, 24, 21, 11, 9, 54, 32, 54, 67, 33]
item1 = 2
item2 = 76
item3 = 24
item4 = 37

print(binarySearch(sequence, item1))
print(binarySearch(sequence, item2))
print(binarySearch(sequence, item3))
print(binarySearch(sequence, item4))
