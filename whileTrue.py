import random

numbers = []

def interface():
    number = random.choice(range(50))
    numbers.append(number)

    return number

while True:
    if interface()%7 == 0:
        break

print(numbers)